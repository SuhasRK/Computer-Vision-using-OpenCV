cmake_minimum_required(VERSION 3.0.0)
project(cpp_test VERSION 0.1.0)

include(CTest)
enable_testing()

find_package(OpenCV REQUIRED )

include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(cpp_test color_picker.cpp)

target_link_libraries(cpp_test ${OpenCV_LIBS})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
