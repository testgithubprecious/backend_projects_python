from manim import *

class RouterTrieScene(Scene):
    def construct(self):
        title = Text("Custom Router Trie Animation", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Step 1: Visualizing the Trie Structure
        root = Circle(radius=0.4, color=BLUE).shift(UP * 2)
        root_label = Text("ROOT", font_size=24).next_to(root, DOWN)
        self.play(FadeIn(root), Write(root_label))

        # First Level
        home = Circle(radius=0.4, color=GREEN).shift(LEFT * 3 + UP)
        home_label = Text("home", font_size=24).next_to(home, DOWN)
        about = Circle(radius=0.4, color=YELLOW).shift(LEFT * 5)
        about_label = Text("about", font_size=24).next_to(about, DOWN)

        user = Circle(radius=0.4, color=GREEN).shift(RIGHT * 3 + UP)
        user_label = Text("user", font_size=24).next_to(user, DOWN)
        var_name = Circle(radius=0.4, color=ORANGE).shift(RIGHT * 5)
        var_label = Text(":name", font_size=24).next_to(var_name, DOWN)

        static = Circle(radius=0.4, color=GREEN).shift(DOWN)
        static_label = Text("static", font_size=24).next_to(static, DOWN)
        wild = Circle(radius=0.4, color=RED).shift(DOWN * 2)
        wild_label = Text("*filepath", font_size=24).next_to(wild, DOWN)

        # Draw edges and nodes
        self.play(
            Create(Line(root.get_center(), home.get_center())),
            Create(Line(root.get_center(), user.get_center())),
            Create(Line(root.get_center(), static.get_center())),
            FadeIn(home), Write(home_label),
            FadeIn(user), Write(user_label),
            FadeIn(static), Write(static_label)
        )

        self.play(
            Create(Line(home.get_center(), about.get_center())),
            FadeIn(about), Write(about_label)
        )

        self.play(
            Create(Line(user.get_center(), var_name.get_center())),
            FadeIn(var_name), Write(var_label)
        )

        self.play(
            Create(Line(static.get_center(), wild.get_center())),
            FadeIn(wild), Write(wild_label)
        )

        self.wait(1)

        # Step 2: Matching Example: "/user/alice"
        match_title = Text("Matching Path: /user/alice", font_size=28).to_edge(UP)
        self.play(Write(match_title))

        # Highlight path: ROOT -> user -> :name
        self.play(
            root.animate.set_fill(BLUE, opacity=0.5),
            user.animate.set_fill(GREEN, opacity=0.5)
        )
        self.wait(0.5)
        self.play(var_name.animate.set_fill(ORANGE, opacity=0.5))
        param_text = Text("Extracted: name = 'alice'", font_size=24).next_to(var_name, RIGHT)
        self.play(Write(param_text))
        self.wait(2)
        self.play(FadeOut(param_text), FadeOut(match_title))

        # Step 3: Matching Example: "/static/js/main.js"
        match2_title = Text("Matching Path: /static/js/main.js", font_size=28).to_edge(UP)
        self.play(Write(match2_title))
        self.play(
            root.animate.set_fill(BLUE, opacity=0.5),
            static.animate.set_fill(GREEN, opacity=0.5)
        )
        self.wait(0.5)
        self.play(wild.animate.set_fill(RED, opacity=0.5))
        param2_text = Text("Extracted: filepath = 'js/main.js'", font_size=24).next_to(wild, RIGHT)
        self.play(Write(param2_text))
        self.wait(2)

        self.play(FadeOut(param2_text), FadeOut(match2_title))

