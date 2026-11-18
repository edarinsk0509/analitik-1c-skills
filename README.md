# Скиллы аналитика 1С

Скиллы для ИИ-агентов (Claude Code, Codex и других), которые помогают аналитику 1С вести анализ, разбирать конфигурацию, готовить данные, писать ТЗ и держать проекты в порядке. Сделаны для курса «От хотелки до ТЗ: аналитик 1С с ИИ-агентом».

Скилл - папка с файлом `SKILL.md`: инструкция, которую агент подключает сам, когда задача подходит под ее описание.

## Что внутри

| Скилл | Что делает |
|---|---|
| `chtz` | Карточка задачи, ЧТЗ на доработку 1С по шаблону и проверка по чек-листу |
| `razvedka-1c` | Разбор алгоритма конфигурации со ссылками на код и проверкой запросом к базе |
| `test-dannye-1c` | Заполнение учебной базы данными через MCP с прогоном на откате |
| `babok-1c` | Бизнес-анализ по BABOK: стейкхолдеры, выявление, требования, трассировка до ЧТЗ, изменения. Артефакты в Markdown |
| `uborka` | Уборка в проекте и синхронизация памяти проекта: CLAUDE.md, README, progress, PRD, KANBAN |
| `proekt` | Реестр проектов по коротким кодам: список, карточка проекта, статусы |
| `permissions-audit` | Разбор разрешений Claude Code: что разрешить постоянно, что оставить под контролем |

`razvedka-1c` и `test-dannye-1c` работают с базой через MCP-сервер 1С (инструменты `execute_query`, `execute_code`, `search_code` и другие). Без MCP `razvedka-1c` работает по выгрузке исходников.

## Установка в Claude Code

Вариант 1. Плагин, в окне Claude Code:

```
/plugin marketplace add edarinsk0509/analitik-1c-skills
/plugin install analitik-1c-skills@analitik-1c-skills
```

Вариант 2. Вручную: скачайте репозиторий и скопируйте нужные папки из `skills\` в `.claude\skills\` своего проекта (или в `%USERPROFILE%\.claude\skills\`, чтобы скиллы были во всех проектах).

## Установка в Codex

Вариант 1. Через `npx skills` (нужен Node.js), в терминале из папки проекта:

```
npx skills add https://github.com/edarinsk0509/analitik-1c-skills
```

Команда спросит, какие скиллы и для какого агента ставить. Так же ставится в Cursor, Copilot, Cline и OpenCode.

Вариант 2. Вручную: скопируйте папки из `skills\` в `.agents\skills\` своего проекта (или в `%USERPROFILE%\.agents\skills\`).

## Проверка

Перезапустите агента и спросите: «какие скиллы тебе доступны». Потом вызовите явно: `/chtz` в Claude Code или «используй скилл chtz» в Codex.

Если скилл не виден: внутри папки скилла должен сразу лежать `SKILL.md`, без лишней вложенной папки.

## Полезные скиллы других авторов

Ставятся по инструкции в их репозиториях.

| Скилл | Автор | Зачем аналитику |
|---|---|---|
| [prd-grill](https://github.com/vasilievyakov/prd-grill) | Яков Васильев, AI Lab | интервью по хотелке раундами вопросов, на выходе мини-PRD |
| [grill-me](https://github.com/mattpocock/skills) | Мэтт Покок | первоисточник prd-grill: агент допрашивает вас по дереву решений |
| [AInalyst](https://t.me/platform_ainalyst) | AInalyst | платформа бизнес-анализа по BABOK с реестром требований через MCP |
| [interview-anonymizer](https://github.com/vasilievyakov/interview-anonymizer) | Яков Васильев, AI Lab | инструмент `anon` и скилл: обезличить данные заказчика до отправки агенту |
| [cc-1c-skills](https://github.com/Nikolay-Shirokov/cc-1c-skills) | Николай Широков | разработка 1С руками агента: расширения, формы, метаданные, обработки |
| [redaktura-skills](https://github.com/N1arko/redaktura-skills) | N1arko | редактура русских текстов: ТЗ и письма заказчику без канцелярита |
| [superpowers](https://github.com/obra/superpowers) | Jesse Vincent | дисциплина работы агента: мозговой штурм, план, проверка перед «готово» |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic | Word, Excel, PDF: ТЗ и таблицы в нужном формате |
| [impeccable](https://github.com/pbakaus/impeccable) | Paul Bakaus | аккуратные HTML-прототипы форм для заказчика |

Установка `anon`:

```
uv tool install https://github.com/vasilievyakov/interview-anonymizer/archive/refs/heads/main.zip
anon install-skill
```

## Лицензия

MIT, см. `LICENSE`.
