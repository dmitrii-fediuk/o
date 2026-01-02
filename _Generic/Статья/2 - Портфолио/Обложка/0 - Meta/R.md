# 
Я хочу опубликовать `᛭A` в качестве элемента своего портфолио на Upwork.
Обозначу этот элемент `Eᨀ`.

#
`Сᨀ` ≔ ⟨ Cover (thumbnail, обложка) для `Eᨀ` ⟩ 

#
`CTᨀ` ≔ ⟨ Текст на `Cᨀ` ⟩ 

#
`Cᨀ-PNG` ≔ ⟪ `Сᨀ` в формате PNG ⟫ ߷⧛.png⧚

#
Я получаю `Cᨀ-PNG` из  `᛭H` следующим скриптом:
```bash
(
	p=$(cygpath -m "$(pwd)")
	o=(
		--screenshot="$p/.png"
		--window-size=1000,800
	)
	chrome-headless-shell "${o[@]}" "file://$p/.html"	
)
```