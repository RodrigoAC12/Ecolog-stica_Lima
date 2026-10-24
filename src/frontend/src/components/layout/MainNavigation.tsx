import type { Page } from '../../types'

export function MainNavigation({ page, navigate }: { page: Page; navigate: (page: Page) => void }) {
  return <nav aria-label="Navegación principal">{(['Inicio', 'Vehículos', 'Pedidos', 'Conductores', 'Clientes'] as Page[]).map(item =>
      <button key={item} type="button" className={page === item ? 'nav-active' : ''} aria-current={page === item ? 'page' : undefined} onClick={() => navigate(item)}>{item}</button>)}</nav>
}
