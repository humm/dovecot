add_executable(testTrajectory testTrajectory.cpp)
target_link_libraries(testTrajectory dmp ${Boost_LIBRARIES})
install(TARGETS testTrajectory DESTINATION bin_test)

add_executable(testDmp testDmp.cpp testDynamicalSystemFunction.cpp)
target_link_libraries(testDmp dmp dynamicalsystems functionapproximators ${Boost_LIBRARIES})
install(TARGETS testDmp DESTINATION bin_test)

add_executable(testDmpSerialization testDmpSerialization.cpp)
target_link_libraries(testDmpSerialization dmp dynamicalsystems functionapproximators ${Boost_LIBRARIES})
install(TARGETS testDmpSerialization DESTINATION bin_test)
