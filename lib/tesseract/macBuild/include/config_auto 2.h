/* include/config_auto.h.  Generated from config.h.in by configure.  */
/* config/config.h.in.  Generated from configure.ac by autoheader.  */


#ifndef CONFIG_AUTO_H
#define CONFIG_AUTO_H
/* config_auto.h: begin */


/* Disable legacy OCR engine */
/* #undef DISABLED_LEGACY_ENGINE */

/* Enable float for LSTM */
#define FAST_FLOAT 1

/* Disable graphics */
/* #undef GRAPHICS_DISABLED */

/* Enable AVX instructions */
#define HAVE_AVX 1

/* Enable AVX2 instructions */
#define HAVE_AVX2 1

/* Define to 1 if you have the <CL/cl.h> header file. */
/* #undef HAVE_CL_CL_H */

/* Define to 1 if you have the <dlfcn.h> header file. */
#define HAVE_DLFCN_H 1

/* Enable FMA instructions */
#define HAVE_FMA 1

/* Define if you have the Accelerate framework */
#define HAVE_FRAMEWORK_ACCELERATE 1

/* Define if you have the OpenCL framework */
#define HAVE_FRAMEWORK_OPENCL 1

/* Define to 1 if you have the <inttypes.h> header file. */
#define HAVE_INTTYPES_H 1

/* Enable libarchive */
#define HAVE_LIBARCHIVE 1

/* Enable libcurl */
#define HAVE_LIBCURL 1

/* Define to 1 if the system has the type `long long int'. */
#define HAVE_LONG_LONG_INT 1

/* Enable NEON instructions */
/* #undef HAVE_NEON */

/* Define to 1 if you have the <OpenCL/cl.h> header file. */
/* #undef HAVE_OPENCL_CL_H */

/* Enable SSE 4.1 instructions */
#define HAVE_SSE4_1 1

/* Define to 1 if you have the <stdint.h> header file. */
#define HAVE_STDINT_H 1

/* Define to 1 if you have the <stdio.h> header file. */
#define HAVE_STDIO_H 1

/* Define to 1 if you have the <stdlib.h> header file. */
#define HAVE_STDLIB_H 1

/* Define to 1 if you have the <strings.h> header file. */
#define HAVE_STRINGS_H 1

/* Define to 1 if you have the <string.h> header file. */
#define HAVE_STRING_H 1

/* Define to 1 if you have the <sys/stat.h> header file. */
#define HAVE_SYS_STAT_H 1

/* Define to 1 if you have the <sys/types.h> header file. */
#define HAVE_SYS_TYPES_H 1

/* Define to 1 if you have the <tensorflow/core/framework/graph.pb.h> header
   file. */
/* #undef HAVE_TENSORFLOW_CORE_FRAMEWORK_GRAPH_PB_H */

/* Define to 1 if you have the <tiffio.h> header file. */
#define HAVE_TIFFIO_H 1

/* Define to 1 if you have the <unistd.h> header file. */
#define HAVE_UNISTD_H 1

/* Define to 1 if the system has the type `wchar_t'. */
#define HAVE_WCHAR_T 1

/* Define to the sub-directory where libtool stores uninstalled libraries. */
#define LT_OBJDIR ".libs/"

/* Name of package */
#define PACKAGE "tesseract"

/* Define to the address where bug reports for this package should be sent. */
#define PACKAGE_BUGREPORT "https://github.com/tesseract-ocr/tesseract/issues"

/* Official date of release */
#define PACKAGE_DATE "11/14"

/* Name of package */
#define PACKAGE_NAME "tesseract"

/* Define to the full name and version of this package. */
#define PACKAGE_STRING "tesseract 5.0.0-rc2-3-gef3bf"

/* Define to the one symbol short name of this package. */
#define PACKAGE_TARNAME "tesseract"

/* Define to the home page for this package. */
#define PACKAGE_URL "https://github.com/tesseract-ocr/tesseract/"

/* Version number */
#define PACKAGE_VERSION "5.0.0-rc2-3-gef3bf"

/* Official year for this release */
#define PACKAGE_YEAR "2021"

/* Define to 1 if all of the C90 standard headers exist (not just the ones
   required in a freestanding environment). This macro is provided for
   backward compatibility; new code need not use it. */
#define STDC_HEADERS 1

/* Version number of package */
#define VERSION "5.0.0-rc2-3-gef3bf"



/* Miscellaneous defines */
#define AUTOCONF 1

/* Not used yet
#ifndef NO_GETTEXT
#define USING_GETTEXT
#endif
*/

/* config_auto.h: end */
#endif

