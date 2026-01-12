https://html.spec.whatwg.org
https://html.spec.whatwg.org/multipage#toc-semantics
https://html.spec.whatwg.org/multipage
https://en.wikipedia.org/wiki/HTML5

**HTML 5.1**, **HTML 5.2** and **HTML 5.3** were **all retired** on 28 January 2021, in favour of the **HTML living standard**.

# article
https://html.spec.whatwg.org/#the-article-element
The article element represents a complete, or self-contained, composition in a document, page, application, or site and that is, in principle, independently distributable or reusable, e.g. in syndication. 
This could be a forum post, a magazine or newspaper article, a blog entry, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.

When article elements are nested, the inner article elements represent articles that are in principle related to the contents of the outer article. 
For instance, a blog entry on a site that accepts user-submitted comments could represent the comments as article elements nested within the article element for the blog entry.

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

# hr
https://html.spec.whatwg.org/#the-hr-element
The hr element represents a paragraph-level thematic break, e.g., a scene change in a story, or a transition to another topic within a section of a reference book; alternatively, it represents a separator between a set of options of a select element.

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

# pre
https://html.spec.whatwg.org/#the-pre-element
The pre element represents a block of preformatted text, in which structure is represented by typographic conventions rather than by elements.

##
To represent a block of computer code, the pre element can be used with a code element; to represent a block of computer output the pre element can be used with a samp element. 
Similarly, the kbd element can be used within a pre element to indicate text that the user is to enter.

# samp
https://html.spec.whatwg.org/#the-samp-element
The samp element represents sample or quoted output from another program or computing system.

# section
https://html.spec.whatwg.org/#the-section-element
The section element represents a generic section of a document or application. 
A section, in this context, is a thematic grouping of content, typically with a heading.

A general rule is that the section element is appropriate only if the element's contents would be listed explicitly in the document's outline.

# var
https://html.spec.whatwg.org/#the-var-element
https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-var-element