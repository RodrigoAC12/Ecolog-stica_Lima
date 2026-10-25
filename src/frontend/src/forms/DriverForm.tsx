import type { FormEvent } from 'react'
import type { Driver } from '../api'
import { Field } from '../components/common/FormField'

type DriverForm = Omit<Driver, 'conductor_id'>

export function DriverFormView({ form, editing, busy, set, submit, onCancel }: {
  form: DriverForm
  editing: string | null
  busy: boolean
  set: <K extends keyof DriverForm>(key: K, value: DriverForm[K]) => void
  submit: (event: FormEvent<HTMLFormElement>) => void
  onCancel: () => void
  
}) {
  return <form onSubmit={submit} className="form-grid">
      <Field label="Nombres"><input required value={form.nombres} onChange={e => set('nombres', e.target.value)} /></Field>
      <Field label="Apellidos"><input required value={form.apellidos} onChange={e => set('apellidos', e.target.value)} /></Field>
      <Field label="Número de licencia"><input required value={form.numero_licencia} onChange={e => set('numero_licencia', e.target.value)} /></Field>
      <Field label="Categoría de licencia"><input required value={form.categoria_licencia} onChange={e => set('categoria_licencia', e.target.value)} /></Field>
      <Field label="Teléfono"><input value={form.telefono ?? ''} onChange={e => set('telefono', e.target.value || null)} /></Field>
      <Field label="Experiencia (años)"><input type="number" min="0" step="1" value={form.experiencia_anios ?? ''} onChange={e => set('experiencia_anios', e.target.value ? Number(e.target.value) : null)} /></Field>
      <Field label="Estado"><select value={form.estado} onChange={e => set('estado', e.target.value)}>
        {['DISPONIBLE', 'ASIGNADO', 'DESCANSO'].map(state => <option key={state}>{state}</option>)}
      </select></Field><div className="actions"><button type="submit" disabled={busy}>{editing ? 'Guardar cambios' : 'Registrar'}</button>
        {editing && <button type="button" className="secondary" onClick={() => { onCancel() }}>Cancelar edición</button>}
      </div>
    </form>
}
