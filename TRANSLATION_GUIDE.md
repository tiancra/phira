# Phira Complete Localization Translation Guide

## Overview
This guide provides complete translations for all 20 FTL files across 13 languages.

## Languages Included
1. **de-DE** - German
2. **en-US** - English
3. **fr-FR** - French
4. **id-ID** - Indonesian
5. **ja-JP** - Japanese
6. **ko-KR** - Korean
7. **pl-PL** - Polish
8. **pt-BR** - Brazilian Portuguese
9. **ru-RU** - Russian
10. **th-TH** - Thai
11. **tr-TR** - Turkish
12. **vi-VN** - Vietnamese
13. **zh-TW** - Traditional Chinese

## Files to Translate
1. cali.ftl - Delay Calibration
2. chapter.ftl - Difficulty Levels
3. chart_order.ftl - Sorting Options
4. collection.ftl - Score Collections
5. common.ftl - Common UI Elements
6. event.ftl - Event Management
7. home.ftl - Home Screen
8. import.ftl - Import Functionality
9. library.ftl - Chart Library
10. local.ftl - Local Charts
11. login.ftl - Authentication
12. message.ftl - Messages
13. multiplayer.ftl - Multiplayer Features
14. profile.ftl - User Profiles
15. rate.ftl - Rating System
16. resource.ftl - Game Resources
17. respack.ftl - Character Skins
18. settings.ftl - Application Settings
19. song.ftl - Song Management
20. tags.ftl - Tag Management

## Important Notes for Translators

### Character Names (DO NOT TRANSLATE)
- **夕 (Shee)** - Main character name. Keep as "Shee" in all languages
- **芙宁娜/芙寧娜** - Translate as "Furina" in all languages (official Honkai: Star Rail localization)

### Product Names (DO NOT TRANSLATE)
- **Phira** - Game name
- **Phira-Furina** - Game version name  
- **Phigros** - Referenced game title
- **TeamFlos** - Creator/developer name

### Technical Elements (PRESERVE EXACTLY)
- Parameter markers: `{ $variable }`
- FTL syntax: Maintain structure and indentation
- Plural forms and conditional logic

## Translation Quality Checklist
- [ ] All 20 files translated for each language
- [ ] Character and product names preserved
- [ ] Parameter markers unchanged
- [ ] FTL file structure maintained
- [ ] Proper localization (not just word-for-word translation)
- [ ] Cultural appropriateness verified
- [ ] Consistency across files

## File Structure
```
phira/locales/
├── de-DE/
├── en-US/
├── fr-FR/
├── id-ID/
├── ja-JP/
├── ko-KR/
├── pl-PL/
├── pt-BR/
├── ru-RU/
├── th-TH/
├── tr-TR/
├── vi-VN/
└── zh-TW/
```

Each directory should contain all 20 .ftl files with appropriate translations.

## Next Steps
1. Review translations for accuracy and cultural appropriateness
2. Test translations in the application
3. Make any corrections needed for game-specific terms
4. Deploy updated locale files to production
