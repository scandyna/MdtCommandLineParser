/****************************************************************************
 **
 ** Copyright (C) 2020-2022 Philippe Steinmann.
 **
 ** This file is part of MdtCommandLineParser library.
 **
 ** MdtCommandLineParser is free software: you can redistribute it and/or modify
 ** it under the terms of the GNU Lesser General Public License as published by
 ** the Free Software Foundation, either version 3 of the License, or
 ** (at your option) any later version.
 **
 ** MdtCommandLineParser is distributed in the hope that it will be useful,
 ** but WITHOUT ANY WARRANTY; without even the implied warranty of
 ** MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 ** GNU Lesser General Public License for more details.
 **
 ** You should have received a copy of the GNU Lesser General Public License
 ** along with MdtCommandLineParser.  If not, see <http://www.gnu.org/licenses/>.
 **
 ****************************************************************************/
#include "Catch2QString.h"
#include <QByteArray>

std::ostream & operator <<(std::ostream & os, const QString & str)
{
  os << str.toLocal8Bit().toStdString();

  return os;
}
