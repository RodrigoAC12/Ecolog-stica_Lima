import { useEffect, useState } from 'react'
import type { Page } from './types'
import { LoginPage } from './pages/LoginPage'
import { HomePage } from './pages/HomePage'
import { VehiclesPage } from './pages/VehiclesPage'
import { OrdersPage } from './pages/OrdersPage'
import { DriversPage } from './pages/DriversPage'
import { ClientsPage } from './pages/ClientsPage'
import { AppHeader } from './components/layout/AppHeader'

export function App() {
  const [token, setToken] = useState('')
  const [page, setPage] = useState<Page>('Inicio')
  useEffect(() => {
    if (token) document.getElementById('main-content')?.focus({ preventScroll: true })
  }, [token, page])
  function navigate(target: Page) {
    setPage(target)
    window.scrollTo(0, 0)
    if (target === page) document.getElementById('main-content')?.focus({ preventScroll: true })
  }
  if (!token) return <LoginPage onLogin={value => { setToken(value); window.scrollTo(0, 0) }} />
  return <div className="app-shell">
    <a className="skip-link" href="#main-content">Saltar al contenido</a>
    <AppHeader page={page} navigate={navigate} onLogout={() => {setToken(''); setPage('Inicio')}} />
    <main id="main-content" tabIndex={-1} className="content">
      {page === 'Inicio' && <HomePage onNavigate={navigate} />}
      {page === 'Vehículos' && <VehiclesPage token={token} />}
      {page === 'Pedidos' && <OrdersPage token={token} />}
      {page === 'Conductores' && <DriversPage token={token} />}
      {page === 'Clientes' && <ClientsPage token={token} />}
    </main>
  </div>
}
