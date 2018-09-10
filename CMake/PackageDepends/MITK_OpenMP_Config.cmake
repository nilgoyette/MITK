find_package(OpenMP REQUIRED)
if(OpemMP_CXX_FOUND)
    list(APPEND ALL_LIBRARIES ${OpenMP_CXX_LIBRARIES})
endif()