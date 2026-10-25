import type { Page } from '../types'

export function HomePage({ onNavigate }: { onNavigate: (page: Page) => void }) {
  const modules: { number: string; title: Page; description: string }[] = [
    { number: '01', title: 'Vehículos', description: 'Gestiona la flota, sus capacidades y estados.' },
    { number: '02', title: 'Pedidos', description: 'Organiza las entregas y sus ventanas de tiempo.' },
    { number: '03', title: 'Conductores', description: 'Consulta quiénes están disponibles para operar.' },
    { number: '04', title: 'Clientes', description: 'Gestiona contactos, preferencias y restricciones de entrega.' },
  ]
  return <section>
    <div className="home-hero"><p className="eyebrow"><span className="eyebrow-mark" /> PANEL / OPERACIÓN LOGÍSTICA</p>
      <h1>Inicio<span className="heading-dot" aria-hidden="true">.</span></h1>
      <p>Un espacio para mantener tu operación en movimiento. Elige un módulo para empezar.</p>
      <div className="hero-decoration" aria-hidden="true"><span>EL</span><i /><i /><i /></div>
    </div>
    <div className="module-section-heading"><div><p className="panel-label">ESPACIO DE TRABAJO</p><h2>Módulos operativos</h2></div><span className="edition-tag">04 MÓDULOS DISPONIBLES</span></div>
    <div className="module-grid">{modules.map(module =>
      <article className="module-card" key={module.number}>
        <div className="module-card-top"><span className="module-index">/{module.number}</span><span className="module-arrow" aria-hidden="true">↗</span></div>
        <h3>{module.title}</h3><p>{module.description}</p>
        <button type="button" className="module-link" onClick={() => onNavigate(module.title)}>Abrir {module.title.toLowerCase()} <span aria-hidden="true">→</span></button>
      </article>
    )}</div>
  </section>
}
