# Description:
# TensorFlow is a computational framework, primarily for use in machine
# learning applications.

load("//tensorflow/core:platform/default/build_config.bzl", "tf_proto_library_py")

package(default_visibility = [":internal"])

licenses(["notice"])  # Apache 2.0

exports_files([
    "LICENSE",
    "ACKNOWLEDGMENTS",
])

# open source marker; do not remove

# Config setting for determining if we are building for Android.
config_setting(
    name = "android",
    values = {
        "crosstool_top": "//external:android/crosstool",
    },
    visibility = ["//visibility:public"],
)

config_setting(
    name = "darwin",
    values = {"cpu": "darwin"},
    visibility = ["//visibility:public"],
)

package_group(
    name = "internal",
    packages = ["//tensorflow/..."],
)

sh_binary(
    name = "swig",
    srcs = ["tools/swig/swig.sh"],
    data = glob(["tools/swig/**"]),
)

filegroup(
    name = "all_files",
    srcs = glob(
        ["**/*"],
        exclude = [
            "**/METADATA",
            "**/OWNERS",
            "g3doc/sitemap.md",
        ],
    ),
    visibility = ["//tensorflow:__subpackages__"],
)

py_library(
    name = "tensorflow_py",
    srcs = ["__init__.py"],
    srcs_version = "PY2AND3",
    visibility = ["//visibility:public"],
    deps = ["//tensorflow/python"],
)

# -------------------------------------------
# New rules should be added above this target.
# -------------------------------------------
cc_binary(
    name = "libtensorflow.so",
    linkshared = 1,
    deps = [
        "//tensorflow/core:tensorflow",
    ],
)

cc_binary(
    name = "libtensorflow_cc.so",
    linkshared = 1,
    deps = [
        "//tensorflow/cc:cc_ops",
        "//tensorflow/core:tensorflow",
    ],
)


tf_proto_library_py(
    name = "extra_actions_base_proto",
    srcs = ["extra_actions_base.proto"],
)

py_binary(
    name = "cmake_py",
    srcs = ["cmake.py"],
    main = "cmake.py",
    data = ["//tensorflow/python:pywrap_tensorflow"],
    deps = ["//google/protobuf:protobuf_python",
            ":extra_actions_base_proto_py",],
)

extra_action(
    name = "cmaker",
    tools = ["//tensorflow:cmake_py"],
    cmd = "$(location :cmake_py) --extra_action_file=$(EXTRA_ACTION_FILE)",
)
action_listener(
    name = "cmake_action",
    mnemonics = ["CppCompile", "CppLinker"],
    extra_actions = ["//tensorflow:cmaker"],
    visibility = ["//visibility:public"],
)

