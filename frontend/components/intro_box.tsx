import { Description, Field, Label, Textarea } from '@headlessui/react'
import clsx from 'clsx'

export default function Example() {
  return (
    <div className="w-full max-w-md px-4">
      <Field disabled>
        <Textarea
          className={clsx(
            'mt-3 block w-full resize-none rounded-lg border-none bg-white/5 py-1.5 px-3 text-sm/6 text-white',
            'focus:outline-none data-[focus]:outline-2 data-[focus]:-outline-offset-2 data-[focus]:outline-white/25',
            'h-80 max-h-80'
          )}
          rows={3}
          placeholder='The AI Assistant for YouTube video analysis helps users quickly extract key information from videos. By processing the video using advanced AI, it transcribes audio, identifies topics, and understands context. Users can input a YouTube URL, ask questions, and receive accurate answers or get summaries of lengthy videos. Designed for students, researchers, and professionals, the AI Assistant simplifies video content navigation and enhances the overall viewing experience.'
        />
      </Field>
    </div>
  )
}
