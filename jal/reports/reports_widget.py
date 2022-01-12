from PySide6.QtCore import Qt, Slot, Signal, QDateTime
from jal.ui.ui_reports_widget import Ui_ReportsWidget
from jal.widgets.helpers import ManipulateDate
from widgets.mdi import MdiWidget
from jal.reports.reports import Reports


# ----------------------------------------------------------------------------------------------------------------------
class ReportsWidget(MdiWidget, Ui_ReportsWidget):
    onClose = Signal()

    def __init__(self, parent=None):
        MdiWidget.__init__(self, parent)
        self.setupUi(self)

        # Setup reports tab
        self.reports = Reports(self.ReportTableView)

        self.connect_signals_and_slots()

    def connect_signals_and_slots(self):
        self.ReportRangeCombo.currentIndexChanged.connect(self.onReportRangeChange)
        self.RunReportBtn.clicked.connect(self.onRunReport)
        self.SaveReportBtn.clicked.connect(self.reports.saveReport)

    @Slot()
    def onReportRangeChange(self, range_index):
        report_ranges = {
            0: lambda: (0, 0),
            1: ManipulateDate.Last3Months,
            2: ManipulateDate.RangeYTD,
            3: ManipulateDate.RangeThisYear,
            4: ManipulateDate.RangePreviousYear
        }
        begin, end = report_ranges[range_index]()
        self.ReportFromDate.setDateTime(QDateTime.fromSecsSinceEpoch(begin, spec=Qt.UTC))
        self.ReportToDate.setDateTime(QDateTime.fromSecsSinceEpoch(end, spec=Qt.UTC))

    @Slot()
    def onRunReport(self):
        pass
