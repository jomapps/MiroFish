import fs from 'fs';
import path from 'path';

export default function translatePlugin(options = {}) {
  const { mapPath } = options;
  let translationMap = {};

  if (fs.existsSync(mapPath)) {
    try {
      translationMap = JSON.parse(fs.readFileSync(mapPath, 'utf-8'));
    } catch (e) {
      console.error('[TranslatePlugin] Failed to parse translation map:', e);
    }
  }

  // Sort keys by length descending to avoid partial matches (longer strings first)
  const sortedKeys = Object.keys(translationMap).sort((a, b) => b.length - a.length);

  return {
    name: 'vite-plugin-translate',
    transform(code, id) {
      // Only process .vue and .js files in the src directory
      if (!id.includes('/src/') || (!id.endsWith('.vue') && !id.endsWith('.js'))) {
        return null;
      }

      let translatedCode = code;
      let count = 0;

      for (const key of sortedKeys) {
        const translation = translationMap[key];
        if (translation && translation.trim() !== '') {
          // Replace occurrences of the Chinese string with the English translation
          // We use a simple replaceAll for now. For more precision, we could use regex 
          // to target text nodes or script strings, but simple replace covers most UI cases.
          const escapedKey = key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
          const regex = new RegExp(escapedKey, 'g');
          
          if (translatedCode.includes(key)) {
            translatedCode = translatedCode.replace(regex, translation);
            count++;
          }
        }
      }

      if (count > 0) {
        // console.log(`[TranslatePlugin] Translated ${count} strings in ${path.basename(id)}`);
      }

      return {
        code: translatedCode,
        map: null // We don't need source maps for this simple transformation
      };
    }
  };
}
