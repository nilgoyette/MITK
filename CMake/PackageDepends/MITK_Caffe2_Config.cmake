find_package(Caffe2 REQUIRED)

list(APPEND ALL_LIBRARIES ${Caffe2_LIBRARIES})
list(APPEND ALL_INCLUDE_DIRECTORIES ${Caffe2_INCLUDE_DIR})

