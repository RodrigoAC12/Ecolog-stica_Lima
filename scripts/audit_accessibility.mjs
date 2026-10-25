import assert from 'node:assert/strict'
import { randomBytes } from 'node:crypto'
import { spawn, spawnSync } from 'node:child_process'
import { createRequire } from 'node:module'
import { mkdir, writeFile } from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const repository = fileURLToPath(new URL('../', import.meta.url))
const frontend = path.join(repository, 'src', 'frontend')
const requireFrontend = createRequire(path.join(frontend, 'package.json'))
const { chromium } = requireFrontend('playwright')
const AxeBuilder = requireFrontend('@axe-core/playwright').default
const runLabel = process.argv[2] || 'actual'
assert.match(runLabel, /^[a-z0-9-]+$/)
const evidenceDirectory = path.join(repository, 'docs', '03 Implementación', 'Sprint 03', 'evidencias')
const temporaryDirectory = path.join(repository, 'tmp', `audit-${Date.now()}-${process.pid}`)
const python = path.join(repository, '.venv', 'Scripts', 'python.exe')
const backendUrl = 'http://127.0.0.1:8003'
const frontendUrl = 'http://127.0.0.1:5175'
const password = randomBytes(24).toString('base64url')
const environment = {
  ...process.env,
  DATABASE_URL: `sqlite:///${path.join(temporaryDirectory, 'test_sprint3.db').replaceAll('\\', '/')}`,
  JWT_SECRET: randomBytes(48).toString('base64url'),
  BOOTSTRAP_OPERATOR_EMAIL: 'operador@sprint3.example.test',
  BOOTSTRAP_OPERATOR_PASSWORD: password,
  VITE_API_PROXY_TARGET: backendUrl,
}
const children = []
let browser
const report = {
  executedAt: new Date().toISOString(),
  label: runLabel,
  scope: 'Aplicación real con API y SQLite aislado, datos sintéticos y navegador Edge sin sesión del usuario.',
  target: 'WCAG 2.2 AA',
  tools: { playwright: requireFrontend('playwright/package.json').version, axePlaywright: requireFrontend('./package-lock.json').packages['node_modules/@axe-core/playwright'].version },
  states: [],
  interactionChecks: [],
  limits: ['No constituye validación humana con lector de pantalla ni aceptación de interesados.', 'Un navegador Chromium no acredita compatibilidad con Firefox ni todas las versiones soportadas.'],
}

async function waitUntilReady(url) {
  for (let attempt = 0; attempt < 60; attempt += 1) {
    try {
      const response = await fetch(url)
      if (response.ok) return
    } catch {}
    await new Promise(resolve => setTimeout(resolve, 500))
  }
  throw new Error(`El servicio de auditoría no respondió: ${url}`)
}

function startProcess(executable, argumentsList, workingDirectory) {
  const child = spawn(executable, argumentsList, { cwd: workingDirectory, env: environment, windowsHide: true, stdio: ['ignore', 'pipe', 'pipe'] })
  children.push(child)
  let errors = ''
  child.stderr.on('data', chunk => { errors = (errors + chunk.toString()).slice(-2000) })
  child.stdout.resume()
  child.on('error', error => { errors = error.message })
  child.on('exit', code => { if (code && code !== 0) process.stderr.write(`Proceso de auditoría finalizado (${code}): ${errors}\n`) })
  return child
}

async function inspectState(page, name, viewport) {
  await page.setViewportSize(viewport)
  await page.waitForTimeout(250)
  const results = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa']).analyze()
  const slug = name.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase()
  const screenshot = `${runLabel}-${slug}-${viewport.width}.png`
  if (['Login', 'Clientes', 'Conductores'].includes(name)) {
    await page.screenshot({ path: path.join(evidenceDirectory, screenshot), fullPage: true })
  }
  const reflow = await page.evaluate(() => ({ viewport: window.innerWidth, content: document.documentElement.scrollWidth, passed: document.documentElement.scrollWidth <= window.innerWidth + 1 }))
  report.states.push({
    name,
    viewport,
    axeVersion: results.testEngine.version,
    rulesPassed: results.passes.length,
    incompleteRules: results.incomplete.map(item => ({ id: item.id, targets: item.nodes.flatMap(node => node.target) })),
    violations: results.violations.map(item => ({ id: item.id, impact: item.impact, description: item.description, help: item.helpUrl, nodes: item.nodes.map(node => ({ target: node.target, summary: node.failureSummary })) })),
    reflow,
    screenshot: ['Login', 'Clientes', 'Conductores'].includes(name) ? screenshot : null,
  })
}

try {
  await mkdir(temporaryDirectory, { recursive: true })
  await mkdir(evidenceDirectory, { recursive: true })
  const initialization = spawnSync(python, ['-c', 'from app.db.base import Base; from app.db.session import engine; import app.models; from app.db.seed_demo import seed; Base.metadata.create_all(engine); seed()'], {
    cwd: path.join(repository, 'src', 'backend'), env: environment, windowsHide: true, encoding: 'utf8',
  })
  assert.equal(initialization.status, 0, initialization.stderr)
  startProcess(python, ['-m', 'uvicorn', 'app.main:app', '--host', '127.0.0.1', '--port', '8003'], path.join(repository, 'src', 'backend'))
  await waitUntilReady(`${backendUrl}/health`)
  startProcess(process.execPath, [path.join(frontend, 'node_modules', 'vite', 'bin', 'vite.js'), '--host', '127.0.0.1', '--port', '5175', '--strictPort'], frontend)
  await waitUntilReady(frontendUrl)
  browser = await chromium.launch({ channel: 'msedge', headless: true })
  report.browser = browser.version()
  const browserContext = await browser.newContext({ viewport: { width: 1440, height: 1000 } })
  const page = await browserContext.newPage()
  await page.goto(frontendUrl)
  await page.getByRole('heading', { name: /Bienvenido de nuevo/ }).waitFor()
  await page.keyboard.press('Tab')
  report.interactionChecks.push({ name: 'Primer Tab alcanza el enlace de salto', passed: await page.getByRole('link', { name: 'Saltar al contenido' }).evaluate(element => element === document.activeElement) })
  await page.keyboard.press('Enter')
  report.interactionChecks.push({ name: 'Enlace de salto mueve el foco al contenido', passed: await page.locator('#main-content').evaluate(element => element === document.activeElement) })
  await page.getByLabel('Correo electrónico').focus()
  report.interactionChecks.push({ name: 'Campo de formulario tiene indicador de foco visible', passed: await page.getByLabel('Correo electrónico').evaluate(element => { const style = getComputedStyle(element); return style.outlineStyle !== 'none' && Number.parseFloat(style.outlineWidth) >= 2 }) })
  await page.locator('h1').click()
  for (const viewport of [{ width: 1440, height: 1000 }, { width: 360, height: 800 }]) await inspectState(page, 'Login', viewport)
  await page.getByLabel('Correo electrónico').fill(environment.BOOTSTRAP_OPERATOR_EMAIL)
  await page.getByLabel('Contraseña').fill(password)
  await page.getByRole('button', { name: 'Ingresar', exact: true }).click()
  await page.getByRole('heading', { name: 'Inicio', exact: true }).waitFor()
  report.interactionChecks.push({ name: 'Inicio de sesión mueve el foco al contenido', passed: await page.locator('#main-content').evaluate(element => element === document.activeElement) })
  for (const name of ['Inicio', 'Vehículos', 'Pedidos', 'Conductores', 'Clientes']) {
    await page.getByRole('navigation').getByRole('button', { name, exact: true }).click()
    await page.getByRole('heading', { name, exact: true }).waitFor()
    report.interactionChecks.push({ name: `Cambio a ${name} mueve el foco al contenido`, passed: await page.locator('#main-content').evaluate(element => element === document.activeElement) })
    for (const viewport of [{ width: 1440, height: 1000 }, { width: 360, height: 800 }]) await inspectState(page, name, viewport)
  }
  await page.setViewportSize({ width: 320, height: 800 })
  report.interactionChecks.push({ name: 'Reflow de clientes a 320 px', passed: await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1) })
  await page.getByRole('button', { name: 'Salir', exact: true }).click()
  await page.getByLabel('Correo electrónico').fill(environment.BOOTSTRAP_OPERATOR_EMAIL)
  await page.getByLabel('Contraseña').fill('intento-incorrecto-de-auditoria')
  await page.getByRole('button', { name: 'Ingresar', exact: true }).click()
  await page.getByRole('alert').waitFor()
  report.interactionChecks.push({ name: 'Error de autenticación se anuncia como alerta', passed: await page.getByRole('alert').isVisible() })
  await inspectState(page, 'LoginError', { width: 360, height: 800 })
  report.summary = {
    states: report.states.length,
    violationOccurrences: report.states.reduce((total, state) => total + state.violations.length, 0),
    uniqueViolations: [...new Set(report.states.flatMap(state => state.violations.map(item => item.id)))],
    failedInteractionChecks: report.interactionChecks.filter(item => !item.passed).length,
    reflowFailures: report.states.filter(state => !state.reflow.passed).length,
  }
  await writeFile(path.join(evidenceDirectory, `accesibilidad-${runLabel}.json`), JSON.stringify(report, null, 2) + '\n')
  process.stdout.write(JSON.stringify(report.summary) + '\n')
} finally {
  await browser?.close()
  for (const child of children.reverse()) child.kill()
}
