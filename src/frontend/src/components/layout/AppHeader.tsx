import type { Page } from '../../types'
import { MainNavigation } from './MainNavigation'

export function AppHeader({ page, navigate, onLogout }: {page: Page; navigate: (page: Page) => void; onLogout: () => void}) {
  return <header className="topbar"><div className="brand"><span className="brand-mark" aria-hidden="true">EL<span>↗</span></span><span>EcoLogística<span className="brand-location">Lima / Perú</span></span></div>
    <MainNavigation page={page} navigate={navigate} />
    <button type="button" className="logout" onClick={onLogout}>Salir</button>
  </header>
}
