import type { FormEvent } from 'react'
import type { Vehicle } from '../api'
import { Field } from '../components/common/FormField'

type VehicleForm = Omit<Vehicle, 'vehiculo_id'>

export function VehicleFormView({ form, editing, busy, set, submit, onCancel }: {
  form: VehicleForm
  editing: string | null
  busy: boolean
  set: <K extends keyof VehicleForm>(key: K, value: VehicleForm[K]) => void
  submit: (event: FormEvent<HTMLFormElement>) => void
  onCancel: () => void
  
}) {
  return <form onSubmit={submit} className="form-grid">
        <Field label="Placa"><input required maxLength={15} value={form.placa} onChange={e => set('placa', e.target.value)} /></Field>
        <Field label="Marca"><input required maxLength={80} value={form.marca} onChange={e => set('marca', e.target.value)} /></Field>
        <Field label="Modelo"><input required maxLength={80} value={form.modelo} onChange={e => set('modelo', e.target.value)} /></Field>
        <Field label="Capacidad (kg)"><input required type="number" step="0.01" min="0.01" value={form.capacidad_kg} onChange={e => set('capacidad_kg', e.target.value)} /></Field>
        <Field label="Capacidad (m³)"><input required type="number" step="0.01" min="0.01" value={form.capacidad_m3} onChange={e => set('capacidad_m3', e.target.value)} /></Field>
        <Field label="Consumo (km/l)"><input type="number" step="0.0001" min="0.0001" value={form.consumo_km_l ?? ''} onChange={e => set('consumo_km_l', e.target.value || null)} /></Field>
        <Field label="Emisión (kg CO₂/km)"><input type="number" step="0.000001" min="0" value={form.factor_emision_kg_co2_km ?? ''} onChange={e => set('factor_emision_kg_co2_km', e.target.value || null)} /></Field>
        <Field label="Estado"><select value={form.estado} onChange={e => set('estado', e.target.value)}>
          {['DISPONIBLE', 'EN_RUTA', 'MANTENIMIENTO', 'INACTIVO'].map(state => <option key={state}>{state}</option>)}
        </select></Field>
        <div className="actions"><button type="submit" disabled={busy}>{editing ? 'Guardar cambios' : 'Registrar'}</button>
          {editing && <button type="button" className="secondary" onClick={() => { onCancel() }}>Cancelar edición</button>}
        </div>
      </form>
}
