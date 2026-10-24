import type { FormEvent } from 'react'
import type { Client } from '../api'
import { Field } from '../components/common/FormField'

type ClientForm = Omit<Client, 'cliente_id' | 'creado_en'>

export function ClientFormView({ form, editing, busy, set, submit, onCancel }: {
  form: ClientForm
  editing: string | null
  busy: boolean
  set: <K extends keyof ClientForm>(key: K, value: ClientForm[K]) => void
  submit: (event: FormEvent<HTMLFormElement>) => void
  onCancel: () => void
  
}) {
  return <form onSubmit={submit} className="form-grid">
        <Field label="Nombre"><input required maxLength={180} value={form.nombre} onChange={e => set('nombre', e.target.value)} /></Field>
        <Field label="Teléfono"><input maxLength={30} value={form.telefono ?? ''} onChange={e => set('telefono', e.target.value || null)} /></Field>
        <Field label="Correo electrónico"><input type="email" maxLength={255} value={form.email ?? ''} onChange={e => set('email', e.target.value || null)} /></Field>
        <Field label="Preferencia de entrega"><textarea maxLength={2000} rows={3} value={form.preferencia_entrega ?? ''} onChange={e => set('preferencia_entrega', e.target.value || null)} /></Field>
        <Field label="Restricción de acceso"><textarea maxLength={2000} rows={3} value={form.restriccion_acceso ?? ''} onChange={e => set('restriccion_acceso', e.target.value || null)} /></Field>
        <Field label="Estado"><select value={form.estado} onChange={e => set('estado', e.target.value as ClientForm['estado'])}><option>ACTIVO</option><option>INACTIVO</option></select></Field>
        <div className="actions"><button disabled={busy}>{editing ? 'Guardar cambios' : 'Registrar'}</button>{editing && <button type="button" className="secondary" onClick={() => { onCancel() }}>Cancelar edición</button>}</div>
      </form>
}
