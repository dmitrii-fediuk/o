Требования к твоему программному коду // ES6

# 1.
Всегде используй синтаксис ES6.

# 2. Примеры правильного форматирования кода
## 2.1.
```javascript
const stopEvent = e => {
    e.preventDefault();
    e.stopPropagation();
    e.stopImmediatePropagation();
};
const openArticle = b => {
    const article = b.closest('article[data-test="JobTile"]');
    if (article) {
        const l = article.querySelector('a[data-test="job-tile-title-link UpLink"]');
        if (l) {
            const u = new URL(l.href);
            const m = u.pathname.match(/_~(\d+)(?=\/|$)/);
            window.open(`${u.origin}/jobs/~${m[1]}`, '_blank');
        }
    }
};
(() => {
    let x = 0, y = 0, article;
    const updateArticle = () => {
        article = document.elementFromPoint(x, y)?.closest('article[data-test="JobTile"]');
    };
    document.addEventListener('mousemove', e => {
        x = e.clientX; y = e.clientY;
        updateArticle();
    }, true);
    document.addEventListener('scroll', updateArticle, true);
    document.addEventListener('keydown', e => {
        if ('Enter' === e.key) {
            stopEvent(e);
            openArticle(article);
        }
    }, true);
})();
document.addEventListener('click', e => {
    const i = e.target;
    const menuItemClass = 'air3-menu-item';
    if (!i.classList.contains(menuItemClass) && e.target.closest('article')) {
        const downBtn = i.closest('button[data-ev-label="dropdown_secondary_toggle"]');
        if (!downBtn) {
            stopEvent(e);
            openArticle(e.target);
        }
        else {
            setTimeout(() => {
                const allItems = document.querySelectorAll('.' + menuItemClass);
                const i = [...allItems].find(i => 'Just not interested' === i.textContent.trim());
                i ? i.click() : null;
            }, 50);
        }
    }
}, true);
```
## 2.2.
```javascript
(() => {
	const p = () => {
		const c = document.querySelector('.conversation-container');
		if (c) {
			const observer = new MutationObserver(mm => {
				mm.forEach(m => {
					if ('attributes' === m.type && 'style' === m.attributeName) {
						c.style.removeProperty('min-height');
					}
				});
			});
			observer.observe(c, {attributes: true, attributeFilter: ['style']});
		}
		return !!c;
	};
	const i = setInterval(() => p() ? clearInterval(i) : null, 50);
})();
```

# 3.
Мои примеры (пункт 2) не являются частью программы, над которой ты работаешь.
Эти примеры лишь показывают требуемое форматирование твоего кода.
Поэтому не копируй эти примеры в своём ответе.