Требования к твоему программному коду // Bash

# 1.
Множество вызываемых из Bash внешних программ обозначу `Bash-Ps`.
Элемент этого множества обозначу `Bash-Pi`.
Все параметры (аргументы, ключи, опции) какой-либо `Bash-Pi` обозначу `Bash-Pi-As`.
Элемент множества `Bash-Pi-As` обозначу `Bash-Pi-Ai`.

# 2.
Если `Bash-Pi` использует 2 формата `Bash-Pi-As`, короткий и длинный, то всегда используй длинный формат.
Например, для `Bash-Pi` `tar` используй `Bash-Pi-Ai` `--extract` вместо `-x`.

# 3.
Вызов `Bash-Pi` обозначу `Bash-Pi-С`.

# 4.
При `Bash-Pi-С` `Bash-Pi-As` должны быть упорядочены по алфафиту.

# 5.
При `Bash-Pi-С` каждый `Bash-Pi-Ai` должен располагаться на новой строке.

# 6.
Если `Bash-Pi-С` использует `Bash-Pi-As`, то передача `Bash-Pi-As` в `Bash-Pi` должна осуществляться объявлением массива следующим образом:
```bash
f1='code'
f2='code-2'
o=(
	--brief
	--recursive
)
diff "${o[@]}" $f2 $f1
```
Этот подход обозначу `Bash-Pi-С-A`.

# 7.
При `Bash-Pi-С-A` по умолчанию называй массив c `Bash-Pi-As` именем `o`.
Если требуется несколько `Bash-Pi-С`, то называй c `Bash-Pi-As` именами `o1`, `o2` и т.д.

# 8. Примеры правильного форматирования кода
## 8.1.
```bash
(
    f1='code'
    f2='code--2025-04-06--14-21'
    o=(
        # 2025-04-08
        # 1) -q
        # 2) «report only when files differ»
        --brief
        --recursive
    )
    diff "${o[@]}" $f2 $f1
)
```
## 8.2.
```bash
(
	ff=(
		'.editorconfig'
		'.gitignore'
		'index.php'
		'pub/index.php'
	)
	p='../patch'
	rm -rf $p
	mkdir -p $p
	chmod -R -v 777 $p			
	for f in "${ff[@]}"; do
		cp --parents $f $p
	done
)
```
## 8.3.
```bash
(
	bin/magento cache:clean
	(
		o=(
			pub/static/*		
			var/cache
			var/page_cache
			var/view_preprocessed
		) 
		rm -rf "${o[@]}"
	)
	(
		locales='en_US es_ES'
		themes=(
			'adminhtml Magento/backend'
			'frontend Hyva/child'
			'frontend Magento/luma'
		)	
		for t in "${themes[@]}"; do
			read -r area theme <<< "$themes"
			o=(
				--area $area
				--force
				--theme $theme
			)
			bin/magento setup:static-content:deploy "${o[@]}" $locales
		done
	)
	bin/magento cache:clean
	(
		cd app/design/frontend/Hyva/child/web/tailwind
		npm run build-prod	
	)		
)	
```
# 9.
Мои примеры (пункт 8) не являются частью программы, над которой ты работаешь.
Эти примеры лишь показывают требуемое форматирование твоего кода.
Поэтому не копируй эти примеры в своём ответе.