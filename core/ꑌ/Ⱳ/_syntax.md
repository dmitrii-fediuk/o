# Ⱳ <var>T</var>
## Syntax
<kbd>Ⱳ <var>T</var></kbd> 
## Meaning
The `ꑌ𝔼` representing the `ꑌꕤ` of the `ꑌ𐏕` which is the `ꑌⱳ_Topic` of the `ꑌⱳ_Article` at `https://en.wikipedia.org/wiki/<T>`.
### Parameters   
- <var>T</var> — the `ꑌURI_Last_Path_Segment` of the `ꑌURI` of the `ꑌⱳ_Article`.
## Example
<kbd>Ⱳ <var>Ontology_(information_science)</var></kbd>  
≡   
<samp>
	An **ontology**:   
	<blockquote>
	a representation, formal naming, and definitions of the categories, properties, and relations between the concepts, data, or entities
	</blockquote>
</samp>

# Ⱳ <var>T₀</var>#<var>T</var>
## Syntax
<kbd>Ⱳ <var>T₀</var>#<var>T</var></kbd> 
## Meaning
The `ꑌ𝔼` representing the `ꑌꕤ` of the `ꑌ𐏕` which is the heading of a particular section of the `ꑌⱳ_Article` at `https://en.wikipedia.org/wiki/<T₀>#<T>`.
### Parameters    
- <var>T</var> — the `ꑌURI_Fragment_Identifier` of the section of the `ꑌⱳ_Article`.
- <var>T₀</var> — the `ꑌURI_Last_Path_Segment` of the `ꑌURI` of the `ꑌⱳ_Article`.
## Example
<kbd>Ⱳ <var>Partially_ordered_set</var>#<var>Intervals</var></kbd>  
≡  
<samp>
	The `ꑌ𝔼` **interval** in the context:   
	<blockquote>
	an <mark>interval</mark> in a poset `P` is a subset that can be defined with interval notation
	</blockquote>
</samp>
## Rationale
This syntax is used when there is no standalone `ꑌⱳ_Article` for the `ꑌ𝔼`. 

# Ⱳ T₀∷T
## Syntax
~~~code
Ⱳ T₀∷T
~~~
## Meaning
The `ꑌ𝔼` representing the `ꑌꕤ` of the `ꑌ𐏕` `T` in the context of the `ꑌⱳ_Article` at `https://en.wikipedia.org/wiki/<T₀>`.
### Parameters    
- <var>T</var> — the `ꑌ𐏕`.
- <var>T₀</var> — the `ꑌURI_Last_Path_Segment` of the `ꑌURI` of the `ꑌⱳ_Article`.  
## Example
<code>Ⱳ Theory_of_categories∷category</code>  
≡   
<samp>
	The `ꑌ𝔼` `category` in the context:   
	<blockquote>
	In ontology, the theory of categories concerns itself with the <mark>categories</mark> of being: the highest genera or kinds of entities.  
	To investigate the categories of being, or simply <mark>categories</mark> <…> 
	</blockquote>
</samp>
## Rationale
Я использую этот синтаксис в тех случаях, когда для описываемого мной `ꑌ𝔼` отсутствует и standalone `ꑌⱳ_Article`, и даже standalone section (with a Fragment Identifier) of a `ꑌⱳ_Article`.

