cmake_minimum_required (VERSION 3.5)

file(GLOB HEADERS
	"bitimage.h"
	"gfx_api.h"
	"gfx_api_gl.h"
	"imd.h"
	"ivisdef.h"
	"jpeg_encoder.h"
	"pieblitfunc.h"
	"pieclip.h"
	"piedef.h"
	"piefunc.h"
	"piematrix.h"
	"piemode.h"
	"pienormalize.h"
	"piepalette.h"
	"piestate.h"
	"pietypes.h"
	"png_util.h"
	"screen.h"
	"tex.h"
	"textdraw.h"
)

file(GLOB SRC
	"bitimage.cpp"
	"gfx_api_gl.cpp"
	"imdload.cpp"
	"jpeg_encoder.cpp"
	"pieblitfunc.cpp"
	"pieclip.cpp"
	"piedraw.cpp"
	"piefunc.cpp"
	"piematrix.cpp"
	"piemode.cpp"
	"piepalette.cpp"
	"piestate.cpp"
	"png_util.cpp"
	"screen.cpp"
	"tex.cpp"
	"textdraw.cpp"
)

find_package(PNG 1.2 REQUIRED)
find_package(OpenGL REQUIRED)
find_package(GLEW 1.5.2 REQUIRED)
find_package(Freetype REQUIRED)
find_package(Harfbuzz 1.0 REQUIRED)

add_library(ivis-opengl ${HEADERS} ${SRC})
set_property(TARGET ivis-opengl PROPERTY FOLDER "lib")
if(WZ_TARGET_ADDITIONAL_PROPERTIES)
	SET_TARGET_PROPERTIES(ivis-opengl PROPERTIES ${WZ_TARGET_ADDITIONAL_PROPERTIES})
endif()
target_include_directories(ivis-opengl PRIVATE ${HARFBUZZ_INCLUDE_DIRS} ${FREETYPE_INCLUDE_DIR_ft2build})
target_link_libraries(ivis-opengl PRIVATE framework PNG::PNG ${HARFBUZZ_LIBRARIES} ${FREETYPE_LIBRARIES})
target_link_libraries(ivis-opengl PUBLIC ${OPENGL_gl_LIBRARY} ${OPENGL_glu_LIBRARY} GLEW::GLEW)

if("${CMAKE_CXX_COMPILER_ID}" MATCHES "GNU")
  if(${CMAKE_CROSSCOMPILING})
    target_compile_definitions(ivis-opengl PUBLIC "GLEW_STATIC")
  endif()
endif()



