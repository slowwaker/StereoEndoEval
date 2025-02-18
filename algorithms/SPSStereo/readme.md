# Edit:
Github Repo Link:  
https://github.com/siposcsaba89/sps-stereo.git  
  
The SPSStereo executable in accessible in /build/Release/spsstereo  
  
To run:  
Open CMD console  
Type "spsstereo.exe images.txt"  
	-Corresponding images.txt files for Hamlyn, SERV-CT, SCARED are located in their respective folders.  

For left images: add "l" to the end of the image name. For example: change "012" -> "012l".  
For right images: Same as above but add "r" instead.  

## SPS-Stereo: Slanted Plane Smoothing Stereo

SPS-Stereo is a dense stereo method employing a slanted plane model. It jointly estimates a superpixel segmentation, boundry labels (such as occlusion boundaries), and a dense depth estimate from a pair of stereo images.

**Citation**  

    @inproceedings{Yamaguchi14,
    author = {Koichiro Yamaguchi and David McAllester and Raquel Urtasun},
    title = {Efficient Joint Segmentation, Occlusion Labeling, Stereo and Flow Estimation},
    booktitle = {ECCV},
    year = {2014}
    }


### Building SPS-Stereo

1. Prerequisites
    * opencv
2. Building
    1. type 'cmake .'
    2. type 'make'


### Usage of demo code

First, download KITTI stereo/flow dataset from [KITTI Vision Benchmark Suite homepage](http://www.cvlibs.net/datasets/kitti/eval_stereo_flow.php?benchmark=stereo) and extract it.

Run SPS-Stereo  
`> ./spsstereo images.txt`

where images.txt looks like:
	left_image_1.png
	right_image_1.png
	..
	left_image_N.png
	right_image_N.png

**Outputs**  

* `000000_10_disp.png`  
Disparity image (PNG 16bit grayscale format)  
(Disparity value) = (Pixel value)/256.0

* `000000_10L_seg.png`  
Segmentation image (PNG 16bit grayscale format)  
(Segment ID) = (Pixel value)

* `000000_10L_plane.png`  
Estimated disparity planes  
the number of lines = the number of segments  
Each line includes parameters of disparity plane of a segment: `(A_i, B_i, C_i)`

* `000000_10L_label.txt`  
Boundary labeling result  
the number of lines = the number of boundaries  
Each line includes three entries: `SegmentID1 SegmentID2 boundary_label`  
`boundary_label`: 0 (Occlusion, SegmentID1 is front), 1 (Occlusion, SegmentID2 is front), 2 (Hinge), 3 (Coplanar)

* `000000_10L_boundary.png`  
Visualization of segmentation result  
Boundary color means a type of relationship between neighboring segments: Red/Blue-Occluion (Red side is front), Green-Hinge, Gray- Coplaner


### License
SPS-Stereo is licensed under the GNU General Public License Version 3 (GPLv3), see [http://www.gnu.org/licenses/gpl.html](http://www.gnu.org/licenses/gpl.html).
