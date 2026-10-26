import type { FormEvent } from 'react'
import type { Order, Client } from '../api'
import { Field } from '../components/common/FormField'

type OrderForm = Omit<Order, 'pedido_id' | 'estado'>

export function OrderFormView({ form, editing, busy, set, submit, onCancel, clients }: {
  form: OrderForm
  editing: string | null
  busy: boolean
  set: <K extends keyof OrderForm>(key: K, value: OrderForm[K]) => void
  submit: (event: FormEvent<HTMLFormElement>) => void
  onCancel: () => void
  clients:Client[];
}) {
  return <form onSubmit={submit} className="form-grid">
        <Field label="Cliente"><select required value={form.cliente_id} onChange={e => set('cliente_id', e.target.value)}>
          <option value="">Selecciona un cliente</option>{clients.map(client => <option value={client.cliente_id} key={client.cliente_id}>{client.nombre}</option>)}
        </select></Field>
        <Field label="Código de pedido"><input required value={form.codigo_pedido} onChange={e => set('codigo_pedido', e.target.value)} /></Field>
        <Field label="Dirección de entrega"><input required value={form.direccion_entrega} onChange={e => set('direccion_entrega', e.target.value)} /></Field>
        <Field label="Referencia"><input value={form.referencia_entrega ?? ''} onChange={e => set('referencia_entrega', e.target.value || null)} /></Field>
        <Field label="Latitud"><input required type="number" step="0.000001" min="-90" max="90" value={form.latitud} onChange={e => set('latitud', e.target.value)} /></Field>
        <Field label="Longitud"><input required type="number" step="0.000001" min="-180" max="180" value={form.longitud} onChange={e => set('longitud', e.target.value)} /></Field>
        <Field label="Peso (kg)"><input required type="number" step="0.01" min="0.01" value={form.peso_kg} onChange={e => set('peso_kg', e.target.value)} /></Field>
        <Field label="Volumen (m³)"><input required type="number" step="0.001" min="0.001" value={form.volumen_m3} onChange={e => set('volumen_m3', e.target.value)} /></Field>
        <Field label="Inicio de ventana"><input required type="datetime-local" value={form.ventana_inicio} onChange={e => set('ventana_inicio', e.target.value)} /></Field>
        <Field label="Fin de ventana"><input required type="datetime-local" value={form.ventana_fin} onChange={e => set('ventana_fin', e.target.value)} /></Field>
        <Field label="Prioridad"><select value={form.prioridad} onChange={e => set('prioridad', e.target.value as OrderForm['prioridad'])}>
          {['ALTA', 'MEDIA', 'BAJA'].map(priority => <option key={priority}>{priority}</option>)}
        </select></Field>
        <Field label="Tipo de producto"><input value={form.tipo_producto ?? ''} onChange={e => set('tipo_producto', e.target.value || null)} /></Field>
        <div className="actions"><button type="submit" disabled={busy || clients.length === 0}>{editing ? 'Guardar cambios' : 'Registrar'}</button>
          {editing && <button type="button" className="secondary" onClick={() => { onCancel() }}>Cancelar edición</button>}
        </div>
      </form>
}
