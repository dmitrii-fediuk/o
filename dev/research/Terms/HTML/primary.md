https://html.spec.whatwg.org
https://html.spec.whatwg.org/multipage#toc-semantics
https://html.spec.whatwg.org/multipage

# article
https://html.spec.whatwg.org/#the-article-element

# h1, h2, h3, h4, h5, h6
https://html.spec.whatwg.org/#the-h1,-h2,-h3,-h4,-h5,-and-h6-elements

# hgroup
https://html.spec.whatwg.org/#the-hgroup-element
The hgroup element represents a heading and related content. 
The element may be used to group an h1–h6 element with one or more p elements containing content representing a subheading, alternative title, or tagline.

# header
https://html.spec.whatwg.org/#the-header-element
The header element represents a group of introductory or navigational aids.

# headingoffset
https://html.spec.whatwg.org/#attr-headingoffset
https://html.spec.whatwg.org/#heading-levels-&-offsets:attr-headingoffset
The headingoffset content attribute allows authors to offset heading levels for descendants.
```html
<body>
	<main>
		<h1>This is a heading level 1</h1>
		<article headingoffset="1">
			<h1>This is a heading level 2</h1>
			<section headingoffset="1">
			<h1>This is a heading level 3</h1>
				<dialog headingreset>
					<h1>This is a heading level 1</h1>
				</dialog>
			</section>
		</article>
		<h1 aria-level="2">This is a heading level 2</h1>
	</main>
</body>
```

# kbd
https://html.spec.whatwg.org/#the-kbd-element
The kbd element represents user input (typically keyboard input, although it may also be used to represent other input, such as voice commands).

When the kbd element is nested inside another kbd element, it represents an actual key or other single unit of input as appropriate for the input mechanism.

# meta
https://html.spec.whatwg.org/#the-meta-element
##
The meta element represents various kinds of metadata that cannot be expressed using the title, base, link, style, and script elements.
##
If a meta element has a name attribute, it sets document metadata.
Document metadata is expressed in terms of name-value pairs, the name attribute on the meta element giving the name, and the content attribute on the same element giving the value. 

# samp
https://html.spec.whatwg.org/#the-samp-element
The samp element represents sample or quoted output from another program or computing system.

# var
https://html.spec.whatwg.org/#the-var-element
https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-var-element