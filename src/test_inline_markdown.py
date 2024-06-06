import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images, split_nodes_image, split_nodes_link, text_to_textnodes
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code, text_type_image, text_type_link
)

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual([TextNode("This is text with a ", text_type_text), TextNode("bolded", text_type_bold), TextNode(" word", text_type_text)], new_nodes)
    
    def test_delim_double_bold(self):
        node = TextNode("This is text with a **bolded** word and **another**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual([TextNode("This is text with a ", text_type_text), TextNode("bolded", text_type_bold), TextNode(" word and ", text_type_text), TextNode("another", text_type_bold)], new_nodes)

    def test_delim_double_bold_multiword(self):
        node = TextNode("This is text with a **bolded word** and **another**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual([TextNode("This is text with a ", text_type_text), TextNode("bolded word", text_type_bold), TextNode(" and ", text_type_text), TextNode("another", text_type_bold)], new_nodes)
    
    def test_delim_italic(self):
        node = TextNode("This is text with a *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual([TextNode("This is text with a ", text_type_text), TextNode("italic", text_type_italic), TextNode(" word", text_type_text)], new_nodes)

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual([TextNode("This is text with a ", text_type_text), TextNode("code block", text_type_code), TextNode(" word", text_type_text)], new_nodes)
    
    def test_extract_image(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_link(self):
        matches = extract_markdown_links("This is text with a [link](https://boot.dev)")
        self.assertListEqual([("link", "https://boot.dev")], matches)
    
    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", text_type_text,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is text with an ", text_type_text), TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png")], new_nodes)
    
    def test_split_link(self):
        node = TextNode("This is text with a [link](https://boot.dev)", text_type_text,)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("This is text with a ", text_type_text), TextNode("link", text_type_link, "https://boot.dev")], new_nodes)

    def test_text_nodes_func(self):
        node = text_to_textnodes("Hi, this is a **bolded** word and *italicized* word and `code block` and here is a [link](https://boot.dev) and an ![image](https://google.photos.com)")
        self.assertListEqual([TextNode("Hi, this is a ", text_type_text), TextNode("bolded", text_type_bold), TextNode(" word and ", text_type_text), TextNode("italicized", text_type_italic), TextNode(" word and ", text_type_text), TextNode("code block", text_type_code), TextNode(" and here is a ", text_type_text), TextNode("link", text_type_link, "https://boot.dev"), TextNode(" and an ", text_type_text), TextNode("image", text_type_image, "https://google.photos.com")], node,)




if __name__ == "__main__":
    unittest.main()

    
