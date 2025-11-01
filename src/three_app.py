
def run():
    scene = __new__(THREE.Scene())
    camera = __new__(THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000))

    renderer = __new__(THREE.WebGLRenderer())
    renderer.setSize(window.innerWidth, window.innerHeight)
    document.getElementById("container").appendChild(renderer.domElement)

    geometry = __new__(THREE.BoxGeometry(1, 1, 1))
    material = __new__(THREE.MeshBasicMaterial({'color': 0x00ff00}))
    cube = __new__(THREE.Mesh(geometry, material))
    scene.add(cube)

    camera.position.z = 5

    def animate():
        requestAnimationFrame(animate)
        cube.rotation.x += 0.01
        cube.rotation.y += 0.01
        renderer.render(scene, camera)

    animate()

run()
