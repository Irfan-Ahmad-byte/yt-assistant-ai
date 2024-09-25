import { Description, Field, Label, Textarea } from '@headlessui/react'
import clsx from 'clsx'

export default function Example() {
  return (
    <div className="w-full max-w-full px-7 mt-10 ">
      <Field disabled>
        <Textarea
          className={clsx(
            'mt-3 block w-full resize-none rounded-lg border-none bg-white/5 py-1.5 px-3 text-sm/6 text-white',
            'focus:outline-none data-[focus]:outline-2 data-[focus]:-outline-offset-2 data-[focus]:outline-white/25',
            'h-96 max-h-96'
          )}
          rows={3}
        />
      </Field>
    </div>
  )
}
