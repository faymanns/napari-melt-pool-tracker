import numpy as np

from napari_melt_pool_tracker import MeltPoolTrackerQWidget


# make_napari_viewer is a pytest fixture that returns a napari viewer object
# capsys is a pytest fixture that captures stdout and stderr output streams
def test_example_q_widget(make_napari_viewer, capsys):
    # make viewer and add an image layer using our fixture
    viewer = make_napari_viewer()
    viewer.add_image(np.random.random((100, 100, 100)), name="test_image")

    # create our widget, passing in the viewer
    widget = MeltPoolTrackerQWidget(viewer)

    # test widget methods
    widget.split_groupbox.comboboxs["Input"].setCurrentText("test_image")
    widget._split()
    widget.speed_pos_groupbox.comboboxs["Input"].setCurrentText("test_image_0")
    widget._determine_laser_speed_and_position()
    widget.window_groupbox.comboboxs["Stack"].setCurrentText("test_image_0")
    widget.window_groupbox.comboboxs["Line"].setCurrentText(
        "test_image_0_line"
    )
    widget._reslice_with_moving_window()
    widget.filter_groupbox.comboboxs["Input"].setCurrentText(
        "test_image_0_resliced"
    )
    widget._filter()
    widget.radial_groupbox.comboboxs["Input"].setCurrentText(
        "test_image_0_resliced_filtered"
    )
    widget._calculate_radial_gradient()
    widget.annotate_surface_groupbox.comboboxs["Input"].setCurrentText(
        "test_image_0_resliced_filtered_radial_gradient"
    )
    widget.annotate_surface_groupbox.comboboxs["Surface"].setCurrentText(
        "test_image_0_resliced_filtered"
    )
    widget._annotate_surface_features()

    # read captured output and check that it's as we expected
    captured = capsys.readouterr()
    assert captured.out == ""
