import { Button, Description, Field, Label, Textarea } from '@headlessui/react'
import clsx from 'clsx'

export default function Example() {
  return (
    <div className="w-full max-w-full px-7 mb-10">
      <Field className="flex items-center">
        <Textarea
          className={clsx(
            'block w-full resize-none rounded-l-lg border-none bg-white/5 px-3 text-sm/6 text-white',
            'focus:outline-none data-[focus]:outline-2 data-[focus]:-outline-offset-2 data-[focus]:outline-white/25',
            'h-12' // Increased height for Textarea
          )}
          rows={1}
          placeholder="Ask your questions related to the YouTube Video."
        />
        <Button className="inline-flex items-center gap-2 rounded-r-lg bg-gray-700 px-3 text-sm/6 font-semibold text-white shadow-inner shadow-white/10 focus:outline-none data-[hover]:bg-gray-600 data-[open]:bg-gray-700 data-[focus]:outline-1 data-[focus]:outline-white h-12">
          Send
        </Button>
      </Field>
    </div>
  )
}
