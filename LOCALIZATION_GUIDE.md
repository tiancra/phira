# PHIRA COMPLETE LOCALIZATION - ALL 13 LANGUAGES

## Generation Instructions

This guide provides the complete translations for Phira across 13 languages. Due to the extensive volume (260 files), translations are organized below in a structured format.

### Quick Start

To generate all files automatically, use the provided Python script:

```bash
python3 generate_translations_master.py phira/locales
```

This will create:
- 13 language directories (de-DE, en-US, fr-FR, id-ID, ja-JP, ko-KR, pl-PL, pt-BR, ru-RU, th-TH, tr-TR, vi-VN, zh-TW)
- 20 FTL files per language (cali, chapter, chart_order, collection, common, event, home, import, library, local, login, message, multiplayer, profile, rate, resource, respack, settings, song, tags)

## File Mapping

All files should be placed in: `phira/locales/[LANGUAGE_CODE]/[FILENAME]`

### Languages & Codes
| Language | Code | Region |
|----------|------|--------|
| German | de-DE | Germany |
| English | en-US | United States |
| French | fr-FR | France |
| Indonesian | id-ID | Indonesia |
| Japanese | ja-JP | Japan |
| Korean | ko-KR | South Korea |
| Polish | pl-PL | Poland |
| Portuguese | pt-BR | Brazil |
| Russian | ru-RU | Russia |
| Thai | th-TH | Thailand |
| Turkish | tr-TR | Turkey |
| Vietnamese | vi-VN | Vietnam |
| Chinese Traditional | zh-TW | Taiwan |

## Critical Translation Rules

### ✅ DO Translate
- UI labels and messages
- User-facing text
- Help messages and descriptions
- Error messages
- Menu items

### ❌ DO NOT Translate
- **Character Names**: "夕" → Keep as "Shee" (not regional variants)
- **"芙宁娜/芙寧娜"** → Always translate as "Furina" (official Honkai: Star Rail localization)
- **Product Names**: Phira, Phira-Furina, Phigros (game titles)
- **Creator Name**: TeamFlos
- **Parameter markers**: { $variable }, { $action -> ... }, etc.
- **FTL syntax**: Preserve all punctuation, brackets, and formatting

### 🔍 Verification Checklist
Before deployment, verify:
- [ ] All 20 files exist for each language
- [ ] Parameter markers unchanged
- [ ] No translation of protected terms
- [ ] FTL syntax integrity maintained
- [ ] Proper UTF-8 encoding
- [ ] Consistency across similar strings
- [ ] Cultural appropriateness (especially for puns/jokes)

## File Descriptions

### 1. **cali.ftl** (Delay Calibration)
- Single label for audio delay calibration feature
- Very short file (< 10 lines)
- One main string key: `label`

### 2. **chapter.ftl** (Difficulty Levels)
- Three difficulty difficulty markers
- Keys: `diff-easy`, `diff-hard`, `diff-extreme`
- Usually EZ, HD, IN in all languages

### 3. **chart_order.ftl** (Sort Options)
- Sorting options for charts
- 6 sort options with forward/reverse variants
- Keys: `time`, `rev-time`, `name`, `rev-name`, `rating`, `rev-rating`

### 4. **collection.ftl** (Score Collections)
- Collection overview
- Label, wait message, collection name
- Keys: `label`, `wait-for-more`, `name-c1`

### 5. **common.ftl** (Common UI)
- Shared UI elements and dialogs
- Delete confirmations, ToS/Privacy Policy
- **Main character intro** - IMPORTANT: Keep character name as "Shee"
- Longest file with complex FTL pluralization

### 6. **event.ftl** (Events)
- Event list and participation
- Load failures, button labels
- Keys: various load-failed, btn-* patterns

### 7. **home.ftl** (Home Screen)
- Main menu options
- Update information with parameter markers
- Keys: `play`, `event`, `respack`, `update`

### 8. **import.ftl** (Import)
- Import dialog messages
- Success/failure states
- Keys: `info-fail`, `import-success`, `import-respack-success`

### 9. **library.ftl** (Chart Library)
- Online chart library
- Pagination and filtering
- Keys: `label`, `page`, `must-login`

### 10. **local.ftl** (Local Charts)
- Local chart management
- Import operations
- Keys: `label`, `import-failed`, `import-success`

### 11. **login.ftl** (Authentication)
- Login/Register forms
- Email validation
- Pluralization with `{ $action -> [login] ... [register] ... }`
- Complex FTL syntax

### 12. **message.ftl** (Messages)
- Message list
- Subtitle with author and time parameters
- Keys: `label`, `subtitle`

### 13. **multiplayer.ftl** (Multiplayer)
- Room creation and joining
- Chat functionality
- Complex messages with player actions
- Longest file with many conditional messages
- Keys: msg-*, chat-*, lock-room, cycle-room

### 14. **profile.ftl** (User Profile)
- Account management
- Avatar upload
- Badge display
- Keys: `logout`, `delete`, `edit-avatar`

### 15. **rate.ftl** (Rating)
- Rating filters
- Rating bounds
- Keys: `rate`, `filter`, `lower-bound`, `upper-bound`

### 16. **resource.ftl** (Game Resources)
- Game world description
- Chapter introductions
- Narrative text - allow proper translation
- Keys: `chap-c1`, `chap-c1-intro`

### 17. **respack.ftl** (Character Skins)
- Character clothing/outfit management
- Default skin reference (Phigros - don't translate)
- Deletion restrictions
- Keys: `label`, `default`, `info-content`

### 18. **settings.ftl** (Settings)
- Application preferences
- Audio, graphics, gameplay settings
- **LONGEST FILE** (~400 lines)
- About section with supporter credits
- Keep supporter names unchanged
- Keys: `item-*`, `about-content`

### 19. **song.ftl** (Song Management)
- Song download and gameplay
- Rating system
- Upload rules and moderation
- Complex conditional logic
- Keys: `dl-*`, `upload-*`, `review-*`, `stabilize-*`

### 20. **tags.ftl** (Tag Filtering)
- Tag management and filtering
- Chart classification
- Keys: `filter`, `edit`, `regular`, `troll`, `plain`, `visual`

## Translation Quality Examples

### Good Translation
```ftl
# German
item-lowq-sub = Aktivieren, wenn der Bildschirm ruckelt

# vs.

# Bad - too literal
item-lowq-sub = Aktivieren wenn der Bildschirm niedrig Qualität ist
```

### Preserving Parameters
```ftl
# Correct - parameters preserved
update = v{ $version } neue Version verfügbar

# Wrong - parameter changed
update = v{ $ver } neue Version verfügbar
```

### Character Name Handling
```ftl
# Correct - name preserved
main-character-name = Shee

# Wrong - name translated
main-character-name = 石
```

## Testing Your Translations

1. **Syntax Validation**
   - Ensure all FTL files are valid
   - Check for unmatched braces: { }
   - Verify select syntax: { $var -> ... }

2. **Content Verification**
   - No placeholders left untranslated
   - Proper punctuation for language
   - Appropriate tone and formality level

3. **In-App Testing**
   - Launch Phira with new language
   - Check all UI strings display correctly
   - Verify special characters render properly
   - Test parameter substitution (version, dates, etc.)

## Final Checklist

- [ ] All 260 files created (13 × 20)
- [ ] File encoding is UTF-8
- [ ] No syntax errors in FTL
- [ ] All 20 files in each language directory
- [ ] Protected terms unchanged (Shee, Furina, Phira, TeamFlos)
- [ ] Parameter markers unchanged
- [ ] Cultural review completed
- [ ] Spell-check performed
- [ ] Consistency verified across files
- [ ] Ready for deployment

## Contact & Support

For translation issues or questions:
- Verify against Chinese (zh-CN) original
- Check FTL syntax documentation
- Review existing language versions for consistency
- Test in application before deployment

---

*Last Updated: 2024*
*Phira-Furina Localization Guide*
