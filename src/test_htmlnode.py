import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_default_init(self):
        node = HTMLNode(tag=None, value=None, children=[], props={})
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})
    
    def test_init_with_parameters(self):
         node = HTMLNode(tag="p", value="Hello World", children=[], props={})
         self.assertEqual(node.tag, "p")
         self.assertEqual(node.value, "Hello World")
         self.assertEqual(node.children, [])
         self.assertEqual(node.props, {})
    
    def test_props_html_conv(self):
        node = HTMLNode(tag="p", value="Hello World", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.props, {"href": "https://www.google.com", "target": "_blank"})


    def test_props_to_html_empty(self):
        node = HTMLNode(tag="", value="")
        self.assertEqual(node.props_to_html(), "")

    
    def test_repr(self):
        node = HTMLNode(tag="a", value="Link", children=[], props={"href": "https://www.google.com"})
        expected_output = "HTMLNode(a, Link, children:[], {'href': 'https://www.google.com'})"
        self.assertEqual(repr(node), expected_output)

# LEAFNODE class

    def test_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

# PARENTNODE class

    def test_to_html_w_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_w_grandchild(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_many_children(self):
        node = ParentNode("p", [LeafNode("b", "Bold Text"), LeafNode(None, "Normal Text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")],)
        self.assertEqual(node.to_html(), "<p><b>Bold Text</b>Normal Text<i>italic text</i>Normal text</p>")
    
    def test_heading(self):
        node = ParentNode("h2", [LeafNode("b", "Bold Text"), LeafNode(None, "Normal Text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")],)
        self.assertEqual(node.to_html(), "<h2><b>Bold Text</b>Normal Text<i>italic text</i>Normal text</h2>")
    
  

if __name__ == "__main__":
    unittest.main()

