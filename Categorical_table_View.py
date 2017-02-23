from PyQt4 import QtCore
Qt = QtCore.Qt


class PandasModel(QtCore.QAbstractTableModel):
	def __init__(self, data, parent=None):
		QtCore.QAbstractTableModel.__init__(self, parent)
		self._data = data

	def rowCount(self, parent=None):
		return len(self._data.values)

	def columnCount(self, parent=None):
		return self._data.columns.size

	def data(self, index, role=QtCore.Qt.DisplayRole):
		if index.isValid():
			if role == QtCore.Qt.DisplayRole:
				return str(self._data.values[index.row()][index.column()])
			if role == Qt.ToolTipRole:
				return str(self._data.values[index.row()][index.column()])
		return None

	def headerData(self, col, orientation, role):
		if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
			return self._data.columns[col]
		return None
