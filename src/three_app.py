
class ThreeApp:

    def __init__(self):
        self.scene = __new__(THREE.Scene())
        self.camera = __new__(THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000))
        self.renderer = __new__(THREE.WebGLRenderer())
        self.renderer.setSize(window.innerWidth, window.innerHeight)
        document.getElementById("container").appendChild(self.renderer.domElement)

        self.shapes = []

        self.ambient_light = __new__(THREE.AmbientLight(0x404040))
        self.scene.add(self.ambient_light)

        self.directional_light = __new__(THREE.DirectionalLight(0xffffff, 0.5))
        self.directional_light.position.set(1, 1, 1)
        self.scene.add(self.directional_light)

        self.camera.position.z = 5

        self.controls = __new__(THREE.OrbitControls(self.camera, self.renderer.domElement))

        self.gui_controls = {
            'color': '#00ff00',
            'rotation_speed': 0.01
        }

        self.gui = __new__(dat.GUI())
        self.gui.addColor(self.gui_controls, 'color').onChange(self.update_color)
        self.gui.add(self.gui_controls, 'rotation_speed', 0, 0.1)

        document.getElementById("add-shape-btn").addEventListener("click", self.add_shape)

        self.add_shape()

        self.animate()

    def add_shape(self):
        shape_select = document.getElementById("shape-select")
        selected_shape = shape_select.value

        if selected_shape == "cube":
            geometry = __new__(THREE.BoxGeometry(1, 1, 1))
        elif selected_shape == "sphere":
            geometry = __new__(THREE.SphereGeometry(0.5, 32, 32))
        elif selected_shape == "torus":
            geometry = __new__(THREE.TorusGeometry(0.5, 0.2, 16, 100))
        elif selected_shape == "cone":
            geometry = __new__(THREE.ConeGeometry(0.5, 1, 32))
        elif selected_shape == "cylinder":
            geometry = __new__(THREE.CylinderGeometry(0.5, 0.5, 1, 32))
        elif selected_shape == "dodecahedron":
            geometry = __new__(THREE.DodecahedronGeometry(0.5))
        else:
            geometry = __new__(THREE.BoxGeometry(1, 1, 1))

        material = __new__(THREE.MeshStandardMaterial({'color': self.gui_controls['color']}))
        new_shape = __new__(THREE.Mesh(geometry, material))
        
        new_shape.position.x = (len(self.shapes) - 1) * 2
        
        self.shapes.append(new_shape)
        self.scene.add(new_shape)

    def update_color(self, value):
        for shape in self.shapes:
            shape.material.color.set(value)

    def animate(self):
        requestAnimationFrame(self.animate)

        for shape in self.shapes:
            shape.rotation.x += self.gui_controls['rotation_speed']
            shape.rotation.y += self.gui_controls['rotation_speed']

        self.controls.update()
        self.stats.update()
        self.renderer.render(self.scene, self.camera)

def run():
    app = ThreeApp()

run()