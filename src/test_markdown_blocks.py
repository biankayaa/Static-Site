import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_blocks(self):
        markdown = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\n* with items'])
    



    def test_multiple_blanks(self):
        markdown = """This is **bolded** paragraph

        

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, ['This is **bolded** paragraph', '', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\n* with items'])



    def test_block_type(self):
        markdowns = ["# Heading", "> This is a quote", "1. First item", "* An unordered item", "This is a paragraph of text."]
        expected_types = ['heading', 'quote', 'ordered list', 'unordered list', 'paragraph']
        for markdown, expected in zip(markdowns, expected_types):
            result = block_to_block_type(markdown)
            self.assertEqual(result, expected)






if __name__ == "__main__":
    unittest.main()