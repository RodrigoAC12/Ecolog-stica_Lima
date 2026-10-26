import type { Notice } from '../../types'

export function NoticeBox({ notice }: { notice: Notice }) {
  return <>
    <div role="status" aria-atomic="true" className={notice && !notice.error ? 'notice success' : undefined}>{notice && !notice.error ? notice.text : ''}</div>
    {notice?.error && <div role="alert" className="notice error">{notice.text}</div>}
  </>
}
