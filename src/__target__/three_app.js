// Transcrypt'ed from Python, 2025-11-01 21:20:38
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, _sort, abs, all, any, assert, bin, bool, bytearray, bytes, callable, chr, delattr, dict, dir, divmod, filter, float, getattr, hasattr, hex, input, int, isinstance, issubclass, len, list, map, max, min, object, oct, ord, pow, print, property, py_TypeError, py_enumerate, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = '__main__';
export var run = function () {
	var scene = new THREE.Scene ();
	var camera = new THREE.PerspectiveCamera (75, window.innerWidth / window.innerHeight, 0.1, 1000);
	var renderer = new THREE.WebGLRenderer ();
	renderer.setSize (window.innerWidth, window.innerHeight);
	document.getElementById ('container').appendChild (renderer.domElement);
	var controls = new THREE.OrbitControls (camera, renderer.domElement);
	var geometry = new THREE.BoxGeometry (1, 1, 1);
	var material = new THREE.MeshBasicMaterial (dict ({'color': 65280}));
	var cube = new THREE.Mesh (geometry, material);
	scene.add (cube);
	camera.position.z = 5;
	var animate = function () {
		requestAnimationFrame (animate);
		controls.py_update ();
		renderer.render (scene, camera);
	};
	animate ();
};
run ();

//# sourceMappingURL=three_app.map