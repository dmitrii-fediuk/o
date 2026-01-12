https://html.spec.whatwg.org
https://html.spec.whatwg.org/multipage#toc-semantics
https://html.spec.whatwg.org/multipage
https://en.wikipedia.org/wiki/HTML5
https://github.com/whatwg/html
https://wiki.whatwg.org/wiki/Rationale
https://wiki.whatwg.org/wiki/Rationale#Versioning_the_spec
https://wiki.whatwg.org
https://whatwg.org/style-guide

#
**HTML 5.1**, **HTML 5.2** and **HTML 5.3** were **all retired** on 28 January 2021, in favour of the **HTML living standard**.

# Why are there no stable snapshots, or versions, of the standard?
https://github.com/whatwg/html/blob/main/FAQ.md#why-are-there-no-stable-snapshots-or-versions-of-the-standard

# What does “Living Standard” mean?
https://whatwg.org/faq#living-standard

# HTML should support a way for anyone to invent new elements!
https://github.com/whatwg/html/blob/main/FAQ.md#html-should-support-a-way-for-anyone-to-invent-new-elements

# abbr
https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-abbr-element
The abbr element represents an abbreviation or acronym, optionally with its expansion. 
##
The title attribute may be used to provide an expansion of the abbreviation. 
The attribute, if specified, must contain an expansion of the abbreviation, and nothing else.

# article
https://html.spec.whatwg.org/#the-article-element
The article element represents a complete, or self-contained, composition in a document, page, application, or site and that is, in principle, independently distributable or reusable, e.g. in syndication. 
This could be a forum post, a magazine or newspaper article, a blog entry, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.

When article elements are nested, the inner article elements represent articles that are in principle related to the contents of the outer article. 
For instance, a blog entry on a site that accepts user-submitted comments could represent the comments as article elements nested within the article element for the blog entry.

# data
https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-data-element
The data element represents its contents, along with a machine-readable form of those contents in the value attribute.
The value attribute must be present. Its value must be a representation of the element's contents in a machine-readable format.

##
When combined with microformats or the microdata attributes defined in this specification, the element serves to provide both a machine-readable value for the purposes of data processors, and a human-readable value for the purposes of rendering in a web browser. 
In this case, the format to be used in the value attribute is determined by the microformats or microdata vocabulary in use.

# dd
https://html.spec.whatwg.org/multipage/grouping-content.html#the-dd-element
The dd element represents the description, definition, or value, part of a term-description group in a description list (dl element).

# details
https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element
The details element represents a disclosure widget from which the user can obtain additional information or controls.

# dfn
https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-dfn-element
The dfn element represents the defining instance of a term. 
The paragraph, description list group, or section that is the nearest ancestor of the dfn element must also contain the definition(s) for the term given by the dfn element.
https://html.spec.whatwg.org/multipage/text-level-semantics.html#defining-term

# dl
https://html.spec.whatwg.org/multipage/grouping-content.html#the-dl-element
In order to annotate groups with microdata attributes, or other global attributes that apply to whole groups, or just for styling purposes, each group in a dl element can be wrapped in a div element. 
This does not change the semantics of the dl element.

# dt
https://html.spec.whatwg.org/multipage/grouping-content.html#the-dt-element
##
The dt element represents the term, or name, part of a term-description group in a description list (dl element).
##
The dt element itself, when used in a dl element, does not indicate that its contents are a term being defined, but this can be indicated using the dfn element.


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

# ins
https://html.spec.whatwg.org/multipage/edits.html#the-ins-element
The ins element represents an addition to the document.

# kbd
https://html.spec.whatwg.org/#the-kbd-element
The kbd element represents user input (typically keyboard input, although it may also be used to represent other input, such as voice commands).

When the kbd element is nested inside another kbd element, it represents an actual key or other single unit of input as appropriate for the input mechanism.

# mark
https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-mark-element
##
The mark element represents a run of text in one document marked or highlighted for reference purposes, due to its relevance in another context. 
##
When used in a quotation or other block of text referred to from the prose, it indicates a highlight that was not originally present but which has been added to bring the reader's attention to a part of the text that might not have been considered important by the original author when the block was originally written, but which is now under previously unexpected scrutiny. 
##
When used in the main prose of a document, it indicates a part of the document that has been highlighted due to its likely relevance to the user's current activity.

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
https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-samp-element
The samp element represents sample or quoted output from another program or computing system.

# section
https://html.spec.whatwg.org/#the-section-element
The section element represents a generic section of a document or application. 
A section, in this context, is a thematic grouping of content, typically with a heading.

A general rule is that the section element is appropriate only if the element's contents would be listed explicitly in the document's outline.

# summary
https://html.spec.whatwg.org/multipage/interactive-elements.html#the-summary-element
The summary element represents a summary, caption, or legend for the rest of the contents of the summary element's parent details element, if any.

# var
https://html.spec.whatwg.org/#the-var-element
https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-var-element
The var element represents a variable. 
This could be an actual variable in a mathematical expression or programming context, an identifier representing a constant, a symbol identifying a physical quantity, a function parameter, or just be a term used as a placeholder in prose.
##
For mathematics, in particular for anything beyond the simplest of expressions, MathML is more appropriate. 
However, the var element can still be used to refer to specific variables that are then mentioned in MathML expressions.