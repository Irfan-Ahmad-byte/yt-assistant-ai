import { Button, Description, Field, Input, Label } from '@headlessui/react'
import clsx from 'clsx'
import Social from './ui/social'
import IntroBox from './intro_box'

export default function Example() {
  return (
    <div className="flex flex-col justify-between h-full">
      <div className="w-full max-w-md px-12 mt-10">
        <Field className="flex items-center">
          <Input
            className={clsx(
              'block w-full rounded-l-lg border-none bg-white/5 py-1.5 px-3 text-sm/6 text-white',
              'focus:outline-none data-[focus]:outline-2 data-[focus]:-outline-offset-2 data-[focus]:outline-white/25',
              'h-12' // Same height for Input
            )}
            placeholder="Paste the URL of the YouTube Video."
          />
          <Button className="inline-flex items-center gap-2 rounded-r-lg bg-gray-700 py-1.5 px-3 text-sm/6 font-semibold text-white shadow-inner shadow-white/10 focus:outline-none data-[hover]:bg-gray-600 data-[open]:bg-gray-700 data-[focus]:outline-1 data-[focus]:outline-white h-12">
            Send
          </Button>
        </Field>
      </div>

      <div className="w-full max-w-md px-4">
        <IntroBox />
      </div>

      <div className="w-full max-w-md px-4">
        <Social border={false} />
      </div>
    </div>
  )
}
