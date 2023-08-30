# Lucene Syntax Usage

## Introduction to Lucene

Lucene is a subproject of Apache Software Foundation's Jakarta project and is an open-source
full-text search engine toolkit. The purpose of Lucene is to provide software developers with
a simple and easy-to-use toolkit for implementing full-text search functionality in their target systems.

## Lucene Syntax

Lucene's syntax allows you to construct search queries in a flexible way to meet different search requirements.
Here is a detailed explanation of Lucene's syntax:

### Keyword Queries

To perform searches with multiple keywords using Lucene syntax, you can use Boolean logical operators
to combine multiple keywords. Lucene supports the following operators:

1. AND operator

    - Use `AND` or `&&` to represent the logical AND relationship.
    - Example: `term1 AND term2` or `term1 && term2`

2. OR operator

    - Use `OR` or `||` to represent the logical OR relationship.
    - Example: `term1 OR term2` or `term1 || term2`

3. NOT operator

    - Use `NOT` or `-` to represent the logical NOT relationship.
    - Example: `term1 NOT term2` or `term1 -term2`

4. Quotes

    - You can enclose a phrase in quotes for exact matching.
    - Example: `"exact phrase"`

#### Examples

1. Specify fields

    ```lucene
    field1:keyword1 AND (field2:keyword2 OR field3:keyword3) NOT field4:keyword4
    ```

    Explanation:

    - The query field `field1` must contain the keyword `keyword1`.
    - Additionally, either the field `field2` must contain the keyword `keyword2` or the field `field3`
      must contain the keyword `keyword3`.
    - Finally, the field `field4` must not contain the keyword `keyword4`.

2. Not specify fields

    ```lucene
    keyword1 AND (keyword2 OR keyword3) NOT keyword4
    ```

    Explanation:

    - The query keyword `keyword1` must exist in any searchable field.
    - Additionally, either the keyword `keyword2` must exist or the keyword `keyword3` must exist in any searchable field.
    - Finally, the keyword `keyword4` must not exist in any searchable field.

### Fuzzy Queries

In Lucene, fuzzy queries can be performed using the tilde (`~`) operator for approximate matching.
You can specify an edit distance to limit the degree of similarity in the matches.

```lucene
term~
```

In the above example, `term` is the keyword to perform a fuzzy match on.

Please note the following:

- After the tilde (`~`), you can optionally specify a parameter to control the similarity of the fuzzy query.
- The parameter value ranges from 0 to 2, where 0 represents an exact match, 1 allows for one edit operation
  (such as adding, deleting, or replacing characters) to match, and 2 allows for two edit operations to match.
- If no parameter value is specified, the default similarity threshold used is 0.5.
- Fuzzy queries will return documents that are similar to the given keyword but may incur some
  performance overhead, especially for larger indexes.

### Wildcards

Lucene supports the following wildcard queries:

1. `*` wildcard: Used to match zero or more characters.

    For example, `te*t` can match "test", "text", "tempest", etc.

2. `?` wildcard: Used to match a single character.

    For example, `te?t` can match "test", "text", etc.

#### Example

```lucene
te?t
```

In the above example, `te?t` represents a word that starts with "te", followed by
any single character, and ends with "t". This query can match words like "test", "text", "tent", etc.

It is important to note that the question mark (`?`) represents only a single character.
If you want to match multiple characters or varying lengths of characters, you can use the
asterisk (`*`) for multi-character wildcard matching. Additionally, the question mark will not match an empty string.

To summarize, in Lucene syntax, the question mark (`?`) is used as a single-character wildcard
to match any single character. By using the question mark in your search keywords, you can
perform more flexible and specific pattern matching.

### Range Queries

Lucene syntax supports range queries, where you can use square brackets `[ ]` or curly braces `{ }`
to represent a range. Here are examples of range queries:

1. Inclusive boundary range query:

    - Square brackets `[ ]` indicate a closed interval that includes the boundary values.
    - Example: `field:[value1 TO value2]` represents the range of values for `field`,
      including both `value1` and `value2`.

2. Exclusive boundary range query:

   - Curly braces `{ }` indicate an open interval that excludes the boundary values.
   - Example: `field:{value1 TO value2}` represents the range of values for `field`
     between `value1` and `value2`, excluding both.

3. Omitted boundary range query:

   - You can omit one or both boundary values to specify an infinite range.
   - Example: `field:[value TO ]` represents the range of values for `field` from `value` to
     positive infinity, and `field:[ TO value]` represents the range of values for `field` from
     negative infinity to `value`.

   !!! note

       Please note that range queries are applicable only to fields that can be sorted,
       such as numeric fields, date fields, etc. Also, ensure that you correctly specify
       the boundary values as the actual value type of the field in your query.
       If you want to perform a range query across the entire index without specifying
       a specific field, you can use the wildcard query `*` instead of a field name.

#### Examples

1. Specify a field

   ```lucene
   timestamp:[2022-01-01 TO 2022-01-31]
   ```

   This will retrieve data where the `timestamp` field falls within the range from January 1, 2022, to January 31, 2022.

2. Not specify a field

   ```lucene
   *:[value1 TO value2]
   ```

   This will search the entire index for documents with values ranging from `value1` to `value2`.
