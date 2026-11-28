## Manimations for ikarus's video I Tried to Animate with Python
from manim import *
from manim.camera.camera import Camera
ikarus_gold = ManimColor.from_rgb((239, 191, 4))
ikarus_purple = ManimColor.from_rgb((20, 2, 30))
class IkarusScene(Scene):
    """Base Scene for Ikarus w/ Purple BG"""
    def __init__(self, renderer = None, camera_class = Camera, always_update_mobjects = False, random_seed = None, skip_animations = False):
        super().__init__(renderer, camera_class, always_update_mobjects, random_seed, skip_animations)
        self.camera.background_color = ikarus_purple
class ExplainingManim(IkarusScene):
    """Explains basic information about Manim"""
    def construct(self):
        ban = ManimBanner()
        txt1 = Text("This is Manim.", font_size = 128).next_to(ban, DOWN)
        txt2 = Text("Mathematical Animation", font_size = 96).move_to([0, 2.5, 0])
        img1 = ImageMobject("python_logo").scale(1.75).move_to([-3.5, -0.5, 0])
        txt3 = Text("Python Library", font_size = 64).next_to(img1, DOWN)
        tri = Triangle(color = ikarus_gold, fill_color = ikarus_gold, fill_opacity = 1).move_to([3.5, -0.5, 0])
        cir = Circle(color = ikarus_gold, fill_color = ikarus_gold, fill_opacity = 1).scale(2).move_to(tri)
        sqr = Square(color = BLUE, fill_color = BLUE, fill_opacity = 1).move_to(cir).rotate(45 * DEGREES)
        txt4 = Text("Smooth, Sleek, Professional", font_size=72)
        txt5 = Text("0", font_size=128).move_to([-5, 2.5, 0])
        arr1 = Arrow(start = [-5, 1.5, 0], end = [-5, -3, 0])
        rct1 = Rectangle(fill_color = ikarus_gold, fill_opacity = 1, height = 1.25, width = 10).next_to(txt5).shift(UP * 0.4, RIGHT * 0.5)
        rct2 = Rectangle(fill_color = ikarus_gold, fill_opacity = 1, height = 1.25, width = 10).next_to(rct1, DOWN)
        rct3 = Rectangle(fill_color = ikarus_gold, fill_opacity = 1, height = 1.25, width = 10).next_to(rct2, DOWN)
        rct4 = Rectangle(fill_color = ikarus_gold, fill_opacity = 1, height = 1.25, width = 10).next_to(rct3, DOWN)
        rct5 = Rectangle(fill_color = ikarus_gold, fill_opacity = 1, height = 1.25, width = 10).next_to(rct4, DOWN)
        rctgroup1 = VGroup(rct1, rct2, rct3, rct4, rct5)
        img2 = ImageMobject("mandelbrot_set").scale(0.7)
        txt6 = Text("The Mandelbrot Set", font_size=96).next_to(img2, DOWN)
        self.play(Write(ban))
        self.play(Write(txt1))
        self.wait(3)
        self.play(FadeOut(ban))
        self.play(Transform(txt1, txt2))
        self.wait(3)
        self.play(Write(txt3))
        self.wait(3)
        self.play(FadeIn(img1))
        self.wait(3)
        self.play(Create(tri))
        self.play(Transform(tri, cir))
        self.play(Transform(tri, sqr))
        self.play(Rotate(tri, 720 * DEGREES, run_time = 4))
        self.wait(3)
        self.play(FadeOut(tri, img1, txt1, txt3))
        self.play(Write(txt4, run_time = 2))
        self.wait(3)
        self.play(Unwrite(txt4), Write(txt5))
        self.play(Create(arr1))
        self.wait(3)
        self.play(Create(rctgroup1, run_time = 2))
        self.wait(3)
        self.play(Uncreate(txt5), Uncreate(arr1))
        self.play(Uncreate(rctgroup1, run_time = 2))
        self.wait(3)
        self.play(FadeIn(img2), Write(txt6))
        self.wait(3)
class InstallingThings(IkarusScene):
    """Showcases a few things required to setup Manim"""
    def construct(self):
        img1 = ImageMobject("Homebrew_logo")
        tex1 = Tex(r"\LaTeX", font_size=192)
        tex2 = Tex(r"$\sum_{k=1}^{n}k^2=\frac{n(n+1)(2n+1)}{6}$", font_size = 128)
        img2 = ImageMobject("package").scale(0.75).shift(UP)
        txt1 = Text("Cairo", font_size=192).next_to(img2, DOWN)
        self.play(FadeIn(img1))
        self.wait(3)
        self.play(FadeOut(img1))
        self.play(Write(tex1))
        self.wait(3)
        self.play(tex1.animate.shift(UP * 2))
        self.play(Write(tex2))
        self.wait(3)
        self.play(FadeOut(tex1, tex2),FadeIn(img2), Write(txt1))
        self.wait(8)
        




