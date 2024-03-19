from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import *

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Constants
        self.sphere_radius = 1.0
        self.sphere_slices = 30
        self.sphere_stacks = 30

        # Camera parameters
        self.camera_distance = 30.0
        self.camera_pitch = 0.0
        self.camera_yaw = 0.0

        # Sphere position
        self.sphere_position = Vec3(0, 0, -5)  # Initial position at the center of the screen

        # Set up lighting
        self.setup_lighting()

        # Load the sphere model
        self.sphere_model = self.loader.loadModel("models/sphere-highpoly.egg")
        self.sphere_model.setScale(self.sphere_radius)
        self.sphere_model.reparentTo(self.render)

        # Set up key events
        self.accept("arrow_left", self.set_move_left, [True])
        self.accept("arrow_left-up", self.set_move_left, [False])
        self.accept("arrow_right", self.set_move_right, [True])
        self.accept("arrow_right-up", self.set_move_right, [False])
        self.accept("arrow_up", self.set_move_forward, [True])
        self.accept("arrow_up-up", self.set_move_forward, [False])
        self.accept("arrow_down", self.set_move_backward, [True])
        self.accept("arrow_down-up", self.set_move_backward, [False])

        # Initialize movement flags
        self.move_forward = False
        self.move_backward = False
        self.move_left = False
        self.move_right = False

        # Task for updating the scene
        self.taskMgr.add(self.update, "update")

    def setup_lighting(self):
        self.directional_light = DirectionalLight("directional_light")
        self.directional_light.setColor(Vec4(1, 1, 1, 1))
        self.directional_light_node_path = self.render.attachNewNode(self.directional_light)
        self.directional_light_node_path.setHpr(0, -60, 0)
        self.render.setLight(self.directional_light_node_path)

        self.ambient_light = AmbientLight("ambient_light")
        self.ambient_light.setColor(Vec4(0.2, 0.2, 0.2, 1))
        self.ambient_light_node_path = self.render.attachNewNode(self.ambient_light)
        self.render.setLight(self.ambient_light_node_path)

    def set_move_left(self, state):
        self.move_left = state

    def set_move_right(self, state):
        self.move_right = state

    def set_move_forward(self, state):
        self.move_forward = state

    def set_move_backward(self, state):
        self.move_backward = state

    def update(self, task):
        dt = globalClock.getDt()

        if self.move_forward:
            self.camera_distance -= 2 * dt
        if self.move_backward:
            self.camera_distance += 2 * dt
        if self.move_left:
            self.sphere_position.setX(self.sphere_position.getX() - 20 * dt)
        if self.move_right:
            self.sphere_position.setX(self.sphere_position.getX() + 20 * dt)

        # Update camera position
        self.camera.setPos(0, -self.camera_distance, 0)

        # Update sphere position
        self.sphere_model.setPos(self.sphere_position)

        return Task.cont

app = MyApp()
app.run()
