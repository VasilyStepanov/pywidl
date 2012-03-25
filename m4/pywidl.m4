AC_DEFUN([AC_CHECK_PYWIDL], [
  succeeded=no

  if test -z "$PYWIDL"; then
    AC_PATH_PROG(PYWIDL, pywidl, no)
  fi

  if test "$PYWIDL" = "no" ; then
    echo "*** The pywidl script could not be found. Make sure it is"
    echo "*** in your path, and is properly installed."
  else
    PYWIDL_VERSION_STRING=`$PYWIDL --version`
    PYWIDL_VERSION=`expr match "$PYWIDL_VERSION_STRING" 'pywidl \\(.*\\)'`
    if test "$1" = "" ; then
      PYWIDL_EXPECTED_VERSION="0.0"
    else
      PYWIDL_EXPECTED_VERSION=$1
    fi
    AC_MSG_CHECKING(for PyWIdl >= $PYWIDL_EXPECTED_VERSION)
      PYWIDL_VERSION_MAJOR=`expr match "$PYWIDL_VERSION" '\\([[0-9]]\\+\\)\\.[[0-9]]\\+'`
      PYWIDL_VERSION_MINOR=`expr match "$PYWIDL_VERSION" '[[0-9]]\\+\\.\\([[0-9]]\\+\\)'`
      PYWIDL_EXPECTED_VERSION_MAJOR=`expr match "$PYWIDL_EXPECTED_VERSION" '\\([[0-9]]\\+\\)\\.[[0-9]]\\+'`
      PYWIDL_EXPECTED_VERSION_MINOR=`expr match "$PYWIDL_EXPECTED_VERSION" '[[0-9]]\\+\\.\\([[0-9]]\\+\\)'`
      VERSION_CHECK=0
      if [[ $PYWIDL_VERSION_MAJOR -gt $PYWIDL_EXPECTED_VERSION_MAJOR ]]; then
        VERSION_CHECK=1
      elif [[ $PYWIDL_VERSION_MAJOR -eq $PYWIDL_EXPECTED_VERSION_MAJOR ]]; then
        if [[ $PYWIDL_VERSION_MINOR -ge $PYWIDL_EXPECTED_VERSION_MINOR ]]; then
          VERSION_CHECK=1
        fi
      fi

      if test "$VERSION_CHECK" = "1" ; then
        AC_MSG_RESULT(yes)
        succeeded=yes
      else
        ## If we have a custom action on failure, don't print errors, but
        ## do set a variable so people can do so.
        ifelse([$3], ,echo "can't find PyWIdl >= $PYWIDL_EXPECTED_VERSION",)
      fi

      AC_SUBST(PYWIDL)
  fi

  if test "$succeeded" = "yes"; then
    ifelse([$2], , :, [$2])
  else
    ifelse([$3], , AC_MSG_ERROR([PyWIdl requirements not met.]), [$3])
  fi
])

