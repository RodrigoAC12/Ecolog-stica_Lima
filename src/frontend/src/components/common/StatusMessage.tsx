import type { Notice } from '../../types'

export function NoticeBox({ notice }: { notice: Notice }) {
  return notice && <div role={notice.error ? 'alert' : 'status'} className={notice.error ? 'notice error' : 'notice success'}>{notice.text}</div>
}
