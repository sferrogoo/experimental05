
class ThreeApp:

    def __init__(self):

        self.scene = __new__(THREE.Scene())

        self.camera = __new__(THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000))

        self.renderer = __new__(THREE.WebGLRenderer())

        self.renderer.setSize(window.innerWidth, window.innerHeight)

        document.getElementById("container").appendChild(self.renderer.domElement)



        self.geometry = __new__(THREE.BoxGeometry(1, 1, 1))

        self.material = __new__(THREE.MeshStandardMaterial({'color': 0x00ff00}))

        self.cube = __new__(THREE.Mesh(self.geometry, self.material))

        self.scene.add(self.cube)



        self.ambient_light = __new__(THREE.AmbientLight(0x404040))

        self.scene.add(self.ambient_light)



        self.directional_light = __new__(THREE.DirectionalLight(0xffffff, 0.5))

        self.directional_light.position.set(1, 1, 1)

        self.scene.add(self.directional_light)



        self.camera.position.z = 5



        self.controls = __new__(THREE.OrbitControls(self.camera, self.renderer.domElement))



        self.stats = __new__(Stats())

        document.body.appendChild(self.stats.dom)



        self.gui_controls = {

            'color': '#00ff00',

            'rotation_speed': 0.01

        }



        self.gui = __new__(dat.GUI())

        self.gui.addColor(self.gui_controls, 'color').onChange(self.update_color)

        self.gui.add(self.gui_controls, 'rotation_speed', 0, 0.1)



        self.animate()



    def update_color(self, value):

        self.cube.material.color.set(value)



    def animate(self):

        requestAnimationFrame(self.animate)



        self.cube.rotation.x += self.gui_controls['rotation_speed']

        self.cube.rotation.y += self.gui_controls['rotation_speed']



        self.controls.update()

        self.stats.update()

        self.renderer.render(self.scene, self.camera)



def run():

    app = ThreeApp()



run()