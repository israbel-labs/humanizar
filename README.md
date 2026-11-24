# Humanizar

Skill para Claude que reescribe textos en español con marcas de escritura con IA, sin cambiar lo que dicen. Es una adaptación al español latinoamericano neutro de [Humanizer](https://github.com/blader/humanizer) 4.0.0.

**Antes:**
> Cabe destacar que la cooperativa se fundó en 1989, convirtiéndose rápidamente en la mayor exportadora de café de la provincia y marcando un antes y un después en la región.

**Después:**
> La cooperativa se fundó en 1989 y en pocos años ya era la mayor exportadora de café de la provincia.

## Qué cambia respecto al original

Los patrones 1 al 26 tienen la misma numeración que el original, para que sea fácil comparar versiones. Todos los ejemplos están en español. Estos cambian de fondo:

| § | Original (inglés) | En esta versión |
|---|---|---|
| 1 | No es X, es Y | "No solo X, sino también Y" cuenta poco cuando las dos mitades son hechos, porque es un correlativo normal en español. |
| 4 | Preámbulos | Incluye las muletillas que anuncian importancia ("cabe destacar que") y el "lo difícil es" que equivale al "the part" del original. |
| 7 | Inicios repetidos con el mismo sujeto | El caso típico es el conector al inicio de cada párrafo: "Además", "Asimismo", "Por otro lado". |
| 8 | Rayas | Se evitan igual, pero la raya es correcta en español, así que una sola pesa poco. Pesa más la raya con espacios, a la inglesa. Se respeta la raya de diálogo en ficción. |
| 10 | Adjetivos compuestos con guion | No aplica al español. Se reemplazó por calcos del inglés: "al final del día", "siéntete libre de", "hacer la diferencia". |
| 11 | Voz pasiva y sujeto omitido | Invertido. En español omitir el sujeto es lo normal; la marca es el pronombre repetido y la pasiva con "fue... por". Se respeta el español caribeño y el "usted". |
| 12 | Vocabulario de IA | Dos listas: palabras que son marca casi siempre y palabras comunes en la prensa y la administración latinoamericanas que solo cuentan si se acumulan. |
| 15 | Frases con -ing | Incluye el gerundio de posterioridad, que los modelos usan para encadenar hechos. La norma solo rechaza el que no tiene relación lógica con el verbo principal, y el skill lo distingue. |
| 18 | Rodeos para no decir ser o tener | Más débil: "cuenta con" es normal en Latinoamérica. |
| 20 | Mayúsculas en títulos | Más fuerte: la norma española pone mayúscula solo en la primera palabra. Incluye días y meses, y la mayúscula después de dos puntos. |
| 21 | Comillas curvas | Unificar el estilo de comillas y poner el punto después de las de cierre, como pide la norma. |
| 22 | Restos de chatbot | Fórmulas en español: "¡Claro que sí!", "Aquí te dejo", "¿En qué más puedo ayudarte?". |

Además agrega tres patrones propios del español, del 27 al 29: adverbios en -mente y "de manera" + adjetivo, verbos de apoyo como "realizar" o "llevar a cabo", y formas de España que se cuelan en un texto latinoamericano. También tiene una sección sobre variante y tratamiento (tú, usted y vos) y una regla para no tocar los formatos de números de cada país.

A diferencia de Humanizer 4.0.0, humanizar sigue sin permitir que la reescritura agregue hechos, aunque el modelo crea que son ciertos.

## Estado

Las listas de vocabulario (§10, §12, §13, §16 y §22) salen de los equivalentes del original, de la versión en portugués de la guía de Wikipedia y de una revisión de las fórmulas que más repiten los modelos en español. Todavía no se contrastaron con un corpus de textos reales. Si encuentras una palabra que sobra o una marca que falta, abre un issue con el ejemplo.

## Instalación

### Claude Code como plugin (recomendado)

```text
/plugin marketplace add israbel-labs/humanizar
/plugin install humanizar@humanizar
```

Para actualizar: `/plugin marketplace update humanizar`. También puedes activar la actualización automática de este marketplace en `/plugin`, pestaña Marketplaces.

### Claude Code como carpeta

Clona el repositorio en tu carpeta de skills personales.

Mac y Linux:

```bash
git clone https://github.com/israbel-labs/humanizar.git ~/.claude/skills/humanizar
```

Windows (PowerShell):

```powershell
git clone https://github.com/israbel-labs/humanizar.git "$HOME\.claude\skills\humanizar"
```

Para actualizar, ejecuta `git pull` dentro de esa carpeta.

### Claude Desktop y claude.ai

Descarga `humanizar.zip` de la [última versión](https://github.com/israbel-labs/humanizar/releases/latest) y súbelo en «Personalizar › Skills». Para actualizar, sube el .zip nuevo.

## Uso

```text
/humanizar

[pega el texto]
```

Si lo instalaste como plugin, el comando puede aparecer como `/humanizar:humanizar`. También puedes pedirlo en lenguaje natural: "Humaniza este texto" o "Haz que no suene a IA". Si das una muestra de tu escritura, el skill imita tu voz.

## Avisos de versión nueva

La primera vez que se usa en una conversación, el skill lee el número de versión del `SKILL.md` publicado en este repositorio y lo compara con el suyo. Si hay una versión más nueva, lo dice en una línea y explica cómo actualizar; luego hace la tarea con la versión instalada. Solo lee el número, no sigue instrucciones del archivo remoto y no se actualiza solo. Sin acceso a la web, la revisión se omite sin aviso. En Claude Code puede pedirte permiso para hacer la consulta la primera vez.

## Mantenimiento

Cuando salga una versión nueva del original, revisa su `CHANGELOG.md` y traslada los cambios que apliquen. Para publicar una versión:

1. Sube el número en `SKILL.md` (en `metadata.version` y en la sección "Versión y actualizaciones") y en `.claude-plugin/plugin.json`.
2. Agrega la entrada en `CHANGELOG.md`.
3. Ejecuta `python scripts/validate.py`. Revisa que las versiones coincidan, que los patrones vayan del 1 al 29 y que cada etiqueta tenga una línea en blanco antes.
4. Ejecuta `python scripts/build_zip.py` y adjunta `dist/humanizar.zip` a la versión en GitHub.

## Archivos

- `SKILL.md`: el skill. Es lo único que lee Claude.
- `LICENSE`: licencia MIT. Conserva el aviso del autor original, como exige la licencia.
- `CHANGELOG.md`: historial de versiones y versión del original en la que se basa.
- `.claude-plugin/`: permite instalarlo como plugin de Claude Code desde GitHub.
- `scripts/`: validación del paquete y armado del .zip.

## Licencia

MIT. Basado en [Humanizer](https://github.com/blader/humanizer) de Siqi Chen. Adaptación de Israbel Labs.
