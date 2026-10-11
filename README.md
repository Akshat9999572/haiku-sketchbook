# Haiku Sketchbook

By **Dr. Akshat Shukla** ? An Educator, Writer. AI Enthusiast.

Double-click **index.html** to open the complete book. It contains every image and its handwriting font and works offline. No install, server or library is required.

## Vercel deployment

Run `npx vercel --prod` from this folder while signed in to Vercel. The included configuration prepares `public/index.html` and publishes only the self-contained sketchbook. The artwork sources and editable template remain in the repository. Run `python build.py` after content changes before deploying again.

Desktop: the book always starts on the front cover. Click the cover or next button to open haiku one. Click the left/right page, use the arrow buttons or arrow keys, or choose a dot. The next click after haiku four turns the final leaf and closes the book on its back cover. Click the closed back cover or the previous button to reopen it. Home opens the front cover; End closes on the back cover. Reverse direction during a flip to reverse its motion. Reduced-motion users skip animation.

Mobile: both covers and four illustrated poems become a vertical reading stack.

## Edit

Edit **sketchbook.template.html**, then run `python build.py` to rebuild the standalone deliverable. The `poems` array contains the text, sketch image, caption, title and alt text. To add another spread, append an entry. You can use a relative image file for new entries, or embed a data URL for a fully portable book. The existing generated artwork is in **assets/**.

The front cover names **Dr. Akshat Shukla**, painted into assets/cover-author.png. The original artwork remains in assets/cover.png. The back cover bio is **An Educator, Writer. AI Enthusiast**. Edit the `author` and `authorBio` constants to change the back cover. Haiku text and annotations are live HTML. Edit the matching header credit separately in the template.

All artwork was generated using the built-in image generation tool. Regeneration prompts are recorded in **ARTWORK.md**. The decorative red seals are abstract artist’s marks. Caveat is distributed under the SIL Open Font License, included in assets/fonts/OFL.txt and the built HTML.

Visual/interaction inspiration: [Matthew Yu’s personal site](https://matthewyu.dev/). This implementation and artwork are original.
