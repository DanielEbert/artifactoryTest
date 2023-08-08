.PHONY: build
build:
	mkdir build || true
	cd build && conan install .. -o fuzzing=True && conan build ..

