       �K"	   Fo��Abrain.Event:2i�k��@      |��	K�Fo��A"�
^
random_uniform/shapeConst*
_output_shapes
:*
valueB:*
dtype0
W
random_uniform/minConst*
_output_shapes
: *
valueB
 *  ��*
dtype0
W
random_uniform/maxConst*
valueB
 *  �?*
dtype0*
_output_shapes
: 
�
random_uniform/RandomUniformRandomUniformrandom_uniform/shape*
dtype0*
_output_shapes
:*
seed2 *

seed *
T0
b
random_uniform/subSubrandom_uniform/maxrandom_uniform/min*
T0*
_output_shapes
: 
p
random_uniform/mulMulrandom_uniform/RandomUniformrandom_uniform/sub*
_output_shapes
:*
T0
b
random_uniformAddrandom_uniform/mulrandom_uniform/min*
_output_shapes
:*
T0
t
Variable
VariableV2*
_output_shapes
:*
	container *
shape:*
shared_name *
dtype0
�
Variable/AssignAssignVariablerandom_uniform*
_class
loc:@Variable*
validate_shape(*
_output_shapes
:*
use_locking(*
T0
e
Variable/readIdentityVariable*
T0*
_class
loc:@Variable*
_output_shapes
:
R
zerosConst*
valueB*    *
dtype0*
_output_shapes
:
v

Variable_1
VariableV2*
shared_name *
dtype0*
_output_shapes
:*
	container *
shape:
�
Variable_1/AssignAssign
Variable_1zeros*
_output_shapes
:*
use_locking(*
T0*
_class
loc:@Variable_1*
validate_shape(
k
Variable_1/readIdentity
Variable_1*
T0*
_class
loc:@Variable_1*
_output_shapes
:
�
mul/yConst*
_output_shapes	
:�*�
value�B��"��z5?6$�=멯�٤3?��G���c�����qbN��U>jhA>A�\?�����>�{�S>��>!�>�H1�dSҼ�O?�=A>��?8���/t�a6?�2��c���;���>���-�ehT�)đ?��>��)?� ���s`?Pj�>s�?"��>Gӥ��5V>.c'?�_�-�5���\��.�6�ﾫ�F��k=K0=g�r=;y0��<����I?r9��vG�?(�9(�=p���P$?�u�>��"<�Q�? ?;.���>y����<˾��U?_�>=j����J?��<�g>-�l?#ݾje׾��ؾ&�?��?ǥ�>A)Y�5�?B|ֽL>|�2?�0�>�x6��1'�Ŭ�>��#=^|?!O��C�=C�=s�����`>1Mþ��=Ҩ��-����?�[?^�>���!c_�Z0���
�ͭ�=$F�>g�ɾ=�%?pC���@;&��>��?�²�v�� Y���?���>2�>��>8L*�7��P�5>M3���J=��8�x�(��}��u�Ⱦ���=��>,I�����/�@>˜?zg��O�q?L��>!��>?�?��Ӿ6�>�1߾|Z�=G�d>�?�>�@���S>��>I�A���=�L���)~?�����L�>>R)>�Ɵ>*)�=�ѾD�>�UR����9����h!?��*�m�9��l��i��>���>2�?���P�>R�r�_/e?�������><�<f�V>��?Q;��wUǾ'$>������i�u�oD;�ߵ���=����Ծ�?��6=��c����}�-?�3�+���A���!�<�F���.�>QG�&�>�a��	�����ɾ���>��Ǿ���V?œ_��T?�I�~eU? fM?)����a�=h�9?7����<�=7�W�J��> 3?��˿ť:�%�S��́>慿Gb�>!�>�d?�����f>S�>`L ?�R�``	�ș��<��7�1?w��=r y��#�>�4?�}�>�?9�3��\��Ǿ�]�=�.�>�mL<��>��6��A
�Փ�ի�>�To��ye�1������,>�X�>Q����l=h[{=����g�R�����4��?�J� 5U>�Ծ��w��>���s��=��:�ܾkԾ\��D,�?C�H?�W�>`]/��t���AY>�u�>= )���?l?|І=e�*�ŉ�����f)m?&�����>O�>��=���pP�>/�!��]�>�#.>-K=����>C��!K��
����U\?�k�akB?^�=e
,=m�u�S$�����=�SR�p�8?
�-�ʖ�>~x���ì>q�?��о�X�'��Ζ�>^��s&����ƽ���VG׾��[�������?��~��d�B>�=����i)=V!��i�|��>T:I��b����g>��>�bc��ᒿ� J=�ܬ�Ы �gQ�p�r�'ͥ?���?\e���@��e��L��m�>%�Q�Ѩ���(��҆>Ip7���?�cb?ܙ�=.�>#�/�<?/BȽO��>Ԏ��y^������Z��{��>�`�E���\
?��8�Y��>�8�>�c����ɾ'V�V��9������8�;'q?��K�#=F%��5�?!����S>5��E�>��?>sh?ߚp?XC?�\&�@{վ).�>R|?2��=/["=C��>�Ȝ�X/������@]�����ɾ��?n��� R=PR/?9&�>���>㱾�5���6��|Z��r�=}�?<�;�uF���G>w(?�H�Z�(�=*��<�����/Oj�l??��\���>B�8��fy�Bw,��;�HP:?��5�ƽ�;޾r*2� �Ip�>���Q�4�m_4�,/?4M�>�w�!ɐ9�Ԗ�$?Z��>��>��[=X}���?aW�����syJ��m����P"@��c�>j�>=��+�O�k��D��P��ϫ��)������ʞ>��/?���� �Q��o�>���)I����=oS�����>�$�2e?-qT�H4���"?3��=��>��T�D��>wK��ąb>�?27�>��z>Ch�=���= n���?����l��mw�|��*�#�С���H@������7�>E�K?��N����#_�>��D?���>�0M�p�z>�s�+�,?n˫> �O=h�	�r
o��\?�	>� ��X�>�an���6?{|"�PL?"Ɵ��6f>#��>R�D>� ��q�\��7�>�1彙�Z>�&�	��>6��>v
�>�cN�x��?���?["=��>ߝ��k��dRξ���>�:v	�oV�?��>첊���M��T�>A*s>�2�>��@��e޼0U_>k��>�,ݾ?�A>����֖��?�=w���1�>>��-=ɟ��2�=m>�^��ՙ���(=ʺ>�����f��<ٸ����> T��ǅ?U>y+�YgV>�t��WZ=q��>���>X�(>��>��T?:,Z?����{����T�>�;F?3Ib�Z�?0��91�=��=n�k��ѱ>�H0���C?�Ȩ��~�<n��-˾X���cA�9+X?Һ׽<*>��������i�?���?���>�?�>�(=!��>����b�?��G��X?ؤH���>��?���>�F?��1��X�>�T=��!?��e>���|֮���ռ�ɽq(����z>�Ü>��%�l{�>n�ξ�Y���j�N�>�u~?���=�,־]Y?O��=O���E���>�T�<`t=��?/d?|<��0?�`�?l@?r?PCƾ$G�>Gj���6����z�=�|�?��H?{��=�?�>;��G
>�i?��?꽭?�~��4��Ҽ��^(�=�3�/h'>��>��>������=~����??n>�Ӿ�h��-����:�E����o������?rN�<�|?��?:��>R􁾪�7?.sw�!��=ց?Ja���_�?g(�6G?C�?jU�>�[>I��	dN���L�	�>���O���?�tM?X	M�J#�<o�!>|Q"==�>_[����& ����?'�G�=>��p�F>�\=���>�?�z���9!?bژ>@w߽�/?�ö>?�>����4#�� 辆i�<%>��u=��=j�:�}d�>	��>�>�E���<X���iV�������g�>_?�<�෾��6�-u���h?�1���o�;I��>�!W>�#���P�tw?�%���`W�M༉'�?�5���˼v�ξ(<��e�оs����X�>�ޚ>3k�^��>� =Ӻ�(Y�=j��>$3��s�@?,_,=;�� �#��7�>�o����0��<U�v>���>� ?�$��5�/?6����뾙����/�<#,H� �~>&Vk>jq>#�F���+>���>Û�=�
+�녬>�W?:8,?y��w"�>82��x�>�5�>?u+���>��(>�ܾ�`�=<��#��?�lJ���V>�,=��w@���={%��5��>{��>��L��l�GS���Y�{�#�+�j>y�?�z?>h��=�W徤��>[���B?��?̖$?Q�ʾ��>�:�>�<P�M*���U?��޾�����<�
��>'ܾm�>j69��p���p�Y�h=de(���<^e*��SJ��g9>�d
?���>4%���?�ܢ>�T����U����n���t,��m�>2��?U V��e?II�7џ���3��hh?|�?h�>Iڂ?su>]& �n7~>�������7f�=uђ>$��>��a��?a��>�E���>@��?�M�>�i˾�G"=Î?����>1M6��ל<-��� ������*���龿���aј���?�<3��>'��?�]:�ᨿ9�>��(�wk�=��(���P�:?v}?����|��?�Y�U��=�pb>��X=�>�2<�|k��I
�D,c���>����2�>iY>���6�3?�^��M�>���>*
dtype0
F
mulMulVariable/readmul/y*
_output_shapes	
:�*
T0
F
addAddmulVariable_1/read*
_output_shapes	
:�*
T0
�
sub/yConst*
_output_shapes	
:�*�
value�B��"��!�>7��>��.>��>�ȋ>BVn>+?�>g^>�$�>f��>.$�>�x�>6�\>I��>}c�>�x�>�j}>���>9n�>6n�>�>�nm>�:�>و�>�Y�>�>'T�>c��>���>+OT>�ʀ>AE�>���>��>.��>�O�>�z�>'��>α�>y��>��>V��>2�>tzZ>b�>�O>�܀>޾k>���>D�>1�>�hd>�T>*��>Q��> Q�>�ha>韝>E�>�8�>m��>�1�>���>�V�>�҂>S�>�ޘ>�k>��>4]�> �7>�k�>�h>��>Iv�>a��>��l>��p>�n�>��>���>1�>��> �>x�>��>!�>�>��w>9��>	Y�>P��>:׉>q�>��>Kͦ>	��>%�>���>篂>s�>��>�p�>lr�>s�> �>�>/�r>W�>�w�>��>��>H{>��m>D�>��>���>�>��>��>���>�>! �>B9�>}�n>���>Ľ>r�>�!>p��>�Q�>�P�>R�`>\��>��>�nP>�Ӈ>�(�>��>2̇>��>��>,��>L^�>���>�X�>=w>��>�P�>�$�>��>�ـ>�S�>v޴>m��>���>a��>�#�>�i�>�z�>2��>��>R�>{ؑ>�&�>��>X�>�ݖ>�]�>�=�>���>/F�>�C>U �>-ܩ>w�>C��>��|>5Y�>$��>k��>Bњ>��>�x>���>ή>���>"�g>�;�>b��>�բ>�[>:�>���>`�>�ƒ>�}T>�>
��>��>_N�>���>1;j>jK�>� �>�ʲ>�Kc>���>y�>b�>��_>E��>K�t>�8{>-E�>ngn>ઠ>zM�>m�D>+��>y	v>hѾ>)��>��>��>���>qP�>l=�>"W�>1��>�v�>��d>�)U>^o3>�՗>��J>)8�>��>qǼ>��>��>dǽ>���>�>~>�o�>L$�>�a�>���>1�>8��>Zռ>Y��>���>NY�>�>���>��~>bפ>1-�>� �>V�>>B�>�Fc>Q�>;��>�E>TӠ>���>�צ>��>�<�>�߈>|�>0��>nB>��>>�^�>.��>]�z>�Ч>�2l>�0q>P�>��>���>MiO>[�>�7�>�N>��> �>R.�>%}�>ʗ�>e�>=�>`׃>P��>>H�>]��>v9�>�M�>��t>v�>��>���>;�>�̌>�ŭ>O�=��>�M}>�{�>�>i��>�u�>�m�>gpZ> �>ax>/!�>���>���>N�><u�>fw>�wY>G�>>��>��>�>�ӧ>^��>��>%��>=�l>R��>��y>Z�>��>.H�>x��>�rU>=ܓ>*}5>��>Y��>�G�>_��>$�>�/�>�r�>���># �>�e>�x�>�b>�J�>��>��>V�2>�}6>N �>,�>#�C>�v?>D��>���>�v�>�pU>��V>d�>���>8��>e�?>�*>:��>>��>�j�>�Z�>qI�>%��>��>��^>�z�>���>x>�>t�}>#h�>���>:QS>��>���>��=>�L�>Pb�>ڽ>���>Y� >��r>'��>�x�>Y��>
�'>���>R��>�I�>)�q>!��>�Bt>�ߦ>}�x>Ծ�>�B�>t��>&,�>g�>],�>O��>���>$�>5{�>�α>#��>dJ~>��>-��>�!>�fE>��>���>�^>Ҽ�>�n�>Av�>)6�>�>��u>�>l�>C�>���>���>��>��w>;��>/Sg>i^�>F�>��v>Ъ�>��>Y�>�r�>u��>��\>�h�>�vO>���>A[�>�j>�ʚ>�i>s��>���>��>6�>f�o>v�X>���>���>q>p�>�9>D&�><T�>���>K�>3aw>q�>}$(>(ʗ>�h>2��>]j>��N>䀘>R�>Q+�>�P�>(c>�x�>!3�>x{<>�A�>��>(�>�ߍ>��Q>�>���>k>�ӵ>*�>�t>��>�u�>Rv�>y>-�z>��>?|�>�Ż>R��>�|�>yo�>��>+�>���>�-�>N�>>��>嬀>��>�6�>6��>+�^>�>��^>��G>�U�>F�>��>ڀ�>��>�^�>g1�>	��>ֱ�>w�>nD�>���>U�>��>a��>��~>'e>­�>i��>���>�v�>�G<>^�>��>N�>ȉ�>�G�>^D�>�>��c>m��>�	�>�c�>�è>�M�>j��>��>wTp>u�>��>g��>�;u>��>�݇>��0>Ӓ�>+�>�"�>W�>'��>�"�>F>>��p>�A�>�x�>J��>��5>:9�>ä>��>qӆ>��>$��>�>���>å>�\�>�k�>fy>�)�>�>�?�>�>6�>b4�>��m>�z>�I�>��:>�!�>�A?>$�>}S�>�Gi>�߫>�$.>a)�>,w�>d�>ä>���>k��>2��>��>v�>��>7��>9�>ѴE>�S�>��>�,�>��b>U�>�%�>�zd>\�>��>�҉>��q>j��>w�l>$~s>Zw�>��z>KՉ>(Ӏ>K�q>�>��>�%�>�>��>���>�>.>"�>�>���>�17>�w�>a��>�>���>)Zu>�:�>���>\w�>��>;(N> �>.��>Oj�>,>+T�>��>Im�>�ѕ>rY>�F�>a{�>�.�>���>�(�>s�s>[n�>�
�>ߟ>�߄>���>�8�>h�>��>M��>���>'��>q�>>��>�S�>M<�>;`�>:P>p��>i�~>侣>�h�>쯺>/v�>t�>�Ҝ>�TY>�t�>B�>�!�>T�>N�>�>:hu>�
�>�א>���>��>f�>�0>��p>ٍ>��>Dd�>1�>�{]>y�B>�v>�4g>��>���>��> P�>�d�>�)�>|.�>ѿ�>�3�>�I>�\�>l��>�'�>�>��R>f�>��>iG�>:إ>�A�>C
�>E4}>4�}>�>�6�>�K�>@_>SP�>&;�>Ij�>e�>��>�؅>�xK>SԻ>ꖉ>��>-|>�>�w>S�>O��>��>+�>k�>�$�>��>x��><D�>���>�P>0�>�8�>��W>sz�>���>�:}>=N�>�>I��>��>�ɢ>�p>Gφ>��>)q�>g�>ɴ�>�p�>���>�te>9b�>+�}>���>�5�>�>�}r>�>�e�>dk�>�MT>긋>�7�>D�>R�>~5z>t~e>sg>�U�>% �>෍>�r.>h��>�:�>�k�>�~�>�>�M�>��>r�>��f>uu{>��>�:�>��|>�c�>H��>Į�>��>Cj�>�>�Na>�"�>�8�>@]�>ʀR>���>Ƙ�>�4�>ln�>�`�>���>;�>+m>؜�>��>f��>.�@>(o�>7�T>��>C<�>�Oo>���>7��>�_>s��>��>�(�>SP}>BX�>R�T>g'h>��>i��>�N�>g,�>�_>X<r>c�>��>Q`N>��>��>ҥ�>��>��>)�i>_�>�bt>�(�>3q�>�b�>�e�>��>�p�>�=T>�c�>�M�>�#�>�É>��=>K��>)�]>N%�>��>��8>�]>��>�b>��>B�>!m_>���>x��>ב�>.��>�.�>�>&�>R��=�Za>^^�>�|�>-��>��>Ax>�>:�Z>�o�>]F>�Z�>bS�>\�>���>Uڴ>vG�>^=�>I�>n/P>�H�>셝>���>j�>�@�>v�>��c>r4�>*�>1�>>R�>¯�>���>O�>��L>pS�>-i�>��>���>R��>�&�>�i�>�59>���><�>#c�>5��>o�>�>F��>kͤ>��>��>^��>�A�>#z�>lk�>���>x�>8�>�0�>�I�>d��>��l>V�>��C>m>j��>���>�ѳ>��>�	�>�+�>��>2/�>�B�>*
dtype0
<
subSubaddsub/y*
_output_shapes	
:�*
T0
;
SquareSquaresub*
_output_shapes	
:�*
T0
O
ConstConst*
_output_shapes
:*
valueB: *
dtype0
Y
MeanMeanSquareConst*
_output_shapes
: *
	keep_dims( *

Tidx0*
T0
R
gradients/ShapeConst*
_output_shapes
: *
valueB *
dtype0
X
gradients/grad_ys_0Const*
valueB
 *  �?*
dtype0*
_output_shapes
: 
o
gradients/FillFillgradients/Shapegradients/grad_ys_0*
T0*

index_type0*
_output_shapes
: 
k
!gradients/Mean_grad/Reshape/shapeConst*
valueB:*
dtype0*
_output_shapes
:
�
gradients/Mean_grad/ReshapeReshapegradients/Fill!gradients/Mean_grad/Reshape/shape*
_output_shapes
:*
T0*
Tshape0
d
gradients/Mean_grad/ConstConst*
valueB:�*
dtype0*
_output_shapes
:
�
gradients/Mean_grad/TileTilegradients/Mean_grad/Reshapegradients/Mean_grad/Const*

Tmultiples0*
T0*
_output_shapes	
:�
`
gradients/Mean_grad/Const_1Const*
_output_shapes
: *
valueB
 *  zD*
dtype0
�
gradients/Mean_grad/truedivRealDivgradients/Mean_grad/Tilegradients/Mean_grad/Const_1*
T0*
_output_shapes	
:�
~
gradients/Square_grad/ConstConst^gradients/Mean_grad/truediv*
valueB
 *   @*
dtype0*
_output_shapes
: 
h
gradients/Square_grad/MulMulsubgradients/Square_grad/Const*
_output_shapes	
:�*
T0
�
gradients/Square_grad/Mul_1Mulgradients/Mean_grad/truedivgradients/Square_grad/Mul*
T0*
_output_shapes	
:�
`
gradients/sub_grad/NegNeggradients/Square_grad/Mul_1*
T0*
_output_shapes	
:�
b
#gradients/sub_grad/tuple/group_depsNoOp^gradients/Square_grad/Mul_1^gradients/sub_grad/Neg
�
+gradients/sub_grad/tuple/control_dependencyIdentitygradients/Square_grad/Mul_1$^gradients/sub_grad/tuple/group_deps*
T0*.
_class$
" loc:@gradients/Square_grad/Mul_1*
_output_shapes	
:�
�
-gradients/sub_grad/tuple/control_dependency_1Identitygradients/sub_grad/Neg$^gradients/sub_grad/tuple/group_deps*
_output_shapes	
:�*
T0*)
_class
loc:@gradients/sub_grad/Neg
c
gradients/add_grad/ShapeConst*
valueB:�*
dtype0*
_output_shapes
:
d
gradients/add_grad/Shape_1Const*
valueB:*
dtype0*
_output_shapes
:
�
(gradients/add_grad/BroadcastGradientArgsBroadcastGradientArgsgradients/add_grad/Shapegradients/add_grad/Shape_1*2
_output_shapes 
:���������:���������*
T0
�
gradients/add_grad/SumSum+gradients/sub_grad/tuple/control_dependency(gradients/add_grad/BroadcastGradientArgs*
_output_shapes	
:�*
	keep_dims( *

Tidx0*
T0
�
gradients/add_grad/ReshapeReshapegradients/add_grad/Sumgradients/add_grad/Shape*
T0*
Tshape0*
_output_shapes	
:�
�
gradients/add_grad/Sum_1Sum+gradients/sub_grad/tuple/control_dependency*gradients/add_grad/BroadcastGradientArgs:1*
_output_shapes
: *
	keep_dims( *

Tidx0*
T0
�
gradients/add_grad/Reshape_1Reshapegradients/add_grad/Sum_1gradients/add_grad/Shape_1*
Tshape0*
_output_shapes
:*
T0
g
#gradients/add_grad/tuple/group_depsNoOp^gradients/add_grad/Reshape^gradients/add_grad/Reshape_1
�
+gradients/add_grad/tuple/control_dependencyIdentitygradients/add_grad/Reshape$^gradients/add_grad/tuple/group_deps*
_output_shapes	
:�*
T0*-
_class#
!loc:@gradients/add_grad/Reshape
�
-gradients/add_grad/tuple/control_dependency_1Identitygradients/add_grad/Reshape_1$^gradients/add_grad/tuple/group_deps*/
_class%
#!loc:@gradients/add_grad/Reshape_1*
_output_shapes
:*
T0
b
gradients/mul_grad/ShapeConst*
valueB:*
dtype0*
_output_shapes
:
e
gradients/mul_grad/Shape_1Const*
_output_shapes
:*
valueB:�*
dtype0
�
(gradients/mul_grad/BroadcastGradientArgsBroadcastGradientArgsgradients/mul_grad/Shapegradients/mul_grad/Shape_1*2
_output_shapes 
:���������:���������*
T0
w
gradients/mul_grad/MulMul+gradients/add_grad/tuple/control_dependencymul/y*
_output_shapes	
:�*
T0
�
gradients/mul_grad/SumSumgradients/mul_grad/Mul(gradients/mul_grad/BroadcastGradientArgs*
	keep_dims( *

Tidx0*
T0*
_output_shapes
: 
�
gradients/mul_grad/ReshapeReshapegradients/mul_grad/Sumgradients/mul_grad/Shape*
_output_shapes
:*
T0*
Tshape0
�
gradients/mul_grad/Mul_1MulVariable/read+gradients/add_grad/tuple/control_dependency*
T0*
_output_shapes	
:�
�
gradients/mul_grad/Sum_1Sumgradients/mul_grad/Mul_1*gradients/mul_grad/BroadcastGradientArgs:1*
_output_shapes	
:�*
	keep_dims( *

Tidx0*
T0
�
gradients/mul_grad/Reshape_1Reshapegradients/mul_grad/Sum_1gradients/mul_grad/Shape_1*
T0*
Tshape0*
_output_shapes	
:�
g
#gradients/mul_grad/tuple/group_depsNoOp^gradients/mul_grad/Reshape^gradients/mul_grad/Reshape_1
�
+gradients/mul_grad/tuple/control_dependencyIdentitygradients/mul_grad/Reshape$^gradients/mul_grad/tuple/group_deps*
T0*-
_class#
!loc:@gradients/mul_grad/Reshape*
_output_shapes
:
�
-gradients/mul_grad/tuple/control_dependency_1Identitygradients/mul_grad/Reshape_1$^gradients/mul_grad/tuple/group_deps*
T0*/
_class%
#!loc:@gradients/mul_grad/Reshape_1*
_output_shapes	
:�
b
GradientDescent/learning_rateConst*
valueB
 *   ?*
dtype0*
_output_shapes
: 
�
4GradientDescent/update_Variable/ApplyGradientDescentApplyGradientDescentVariableGradientDescent/learning_rate+gradients/mul_grad/tuple/control_dependency*
use_locking( *
T0*
_class
loc:@Variable*
_output_shapes
:
�
6GradientDescent/update_Variable_1/ApplyGradientDescentApplyGradientDescent
Variable_1GradientDescent/learning_rate-gradients/add_grad/tuple/control_dependency_1*
_output_shapes
:*
use_locking( *
T0*
_class
loc:@Variable_1
�
GradientDescentNoOp5^GradientDescent/update_Variable/ApplyGradientDescent7^GradientDescent/update_Variable_1/ApplyGradientDescent
\
cost_scalar/tagsConst*
valueB Bcost_scalar*
dtype0*
_output_shapes
: 
U
cost_scalarScalarSummarycost_scalar/tagsMean*
T0*
_output_shapes
: 
P
Merge/MergeSummaryMergeSummarycost_scalar*
N*
_output_shapes
: 
2
initNoOp^Variable/Assign^Variable_1/Assign"\n�I      �jO�	U	Fo��AJ��
��
:
Add
x"T
y"T
z"T"
Ttype:
2	
�
ApplyGradientDescent
var"T�

alpha"T

delta"T
out"T�" 
Ttype:
2	"
use_lockingbool( 
x
Assign
ref"T�

value"T

output_ref"T�"	
Ttype"
validate_shapebool("
use_lockingbool(�
R
BroadcastGradientArgs
s0"T
s1"T
r0"T
r1"T"
Ttype0:
2	
8
Const
output"dtype"
valuetensor"
dtypetype
^
Fill
dims"
index_type

value"T
output"T"	
Ttype"

index_typetype0:
2	
.
Identity

input"T
output"T"	
Ttype
�
Mean

input"T
reduction_indices"Tidx
output"T"
	keep_dimsbool( " 
Ttype:
2	"
Tidxtype0:
2	
8
MergeSummary
inputs*N
summary"
Nint(0
=
Mul
x"T
y"T
z"T"
Ttype:
2	�
.
Neg
x"T
y"T"
Ttype:

2	

NoOp
~
RandomUniform

shape"T
output"dtype"
seedint "
seed2int "
dtypetype:
2"
Ttype:
2	�
>
RealDiv
x"T
y"T
z"T"
Ttype:
2	
[
Reshape
tensor"T
shape"Tshape
output"T"	
Ttype"
Tshapetype0:
2	
P
ScalarSummary
tags
values"T
summary"
Ttype:
2	
1
Square
x"T
y"T"
Ttype:

2	
:
Sub
x"T
y"T
z"T"
Ttype:
2	
�
Sum

input"T
reduction_indices"Tidx
output"T"
	keep_dimsbool( " 
Ttype:
2	"
Tidxtype0:
2	
c
Tile

input"T
	multiples"
Tmultiples
output"T"	
Ttype"

Tmultiplestype0:
2	
s

VariableV2
ref"dtype�"
shapeshape"
dtypetype"
	containerstring "
shared_namestring �*1.10.12v1.10.1-0-g4dcfddc5d1�
^
random_uniform/shapeConst*
valueB:*
dtype0*
_output_shapes
:
W
random_uniform/minConst*
valueB
 *  ��*
dtype0*
_output_shapes
: 
W
random_uniform/maxConst*
valueB
 *  �?*
dtype0*
_output_shapes
: 
�
random_uniform/RandomUniformRandomUniformrandom_uniform/shape*

seed *
T0*
dtype0*
_output_shapes
:*
seed2 
b
random_uniform/subSubrandom_uniform/maxrandom_uniform/min*
T0*
_output_shapes
: 
p
random_uniform/mulMulrandom_uniform/RandomUniformrandom_uniform/sub*
T0*
_output_shapes
:
b
random_uniformAddrandom_uniform/mulrandom_uniform/min*
T0*
_output_shapes
:
t
Variable
VariableV2*
shape:*
shared_name *
dtype0*
_output_shapes
:*
	container 
�
Variable/AssignAssignVariablerandom_uniform*
use_locking(*
T0*
_class
loc:@Variable*
validate_shape(*
_output_shapes
:
e
Variable/readIdentityVariable*
T0*
_class
loc:@Variable*
_output_shapes
:
R
zerosConst*
dtype0*
_output_shapes
:*
valueB*    
v

Variable_1
VariableV2*
dtype0*
_output_shapes
:*
	container *
shape:*
shared_name 
�
Variable_1/AssignAssign
Variable_1zeros*
validate_shape(*
_output_shapes
:*
use_locking(*
T0*
_class
loc:@Variable_1
k
Variable_1/readIdentity
Variable_1*
T0*
_class
loc:@Variable_1*
_output_shapes
:
�
mul/yConst*
dtype0*
_output_shapes	
:�*�
value�B��"��z5?6$�=멯�٤3?��G���c�����qbN��U>jhA>A�\?�����>�{�S>��>!�>�H1�dSҼ�O?�=A>��?8���/t�a6?�2��c���;���>���-�ehT�)đ?��>��)?� ���s`?Pj�>s�?"��>Gӥ��5V>.c'?�_�-�5���\��.�6�ﾫ�F��k=K0=g�r=;y0��<����I?r9��vG�?(�9(�=p���P$?�u�>��"<�Q�? ?;.���>y����<˾��U?_�>=j����J?��<�g>-�l?#ݾje׾��ؾ&�?��?ǥ�>A)Y�5�?B|ֽL>|�2?�0�>�x6��1'�Ŭ�>��#=^|?!O��C�=C�=s�����`>1Mþ��=Ҩ��-����?�[?^�>���!c_�Z0���
�ͭ�=$F�>g�ɾ=�%?pC���@;&��>��?�²�v�� Y���?���>2�>��>8L*�7��P�5>M3���J=��8�x�(��}��u�Ⱦ���=��>,I�����/�@>˜?zg��O�q?L��>!��>?�?��Ӿ6�>�1߾|Z�=G�d>�?�>�@���S>��>I�A���=�L���)~?�����L�>>R)>�Ɵ>*)�=�ѾD�>�UR����9����h!?��*�m�9��l��i��>���>2�?���P�>R�r�_/e?�������><�<f�V>��?Q;��wUǾ'$>������i�u�oD;�ߵ���=����Ծ�?��6=��c����}�-?�3�+���A���!�<�F���.�>QG�&�>�a��	�����ɾ���>��Ǿ���V?œ_��T?�I�~eU? fM?)����a�=h�9?7����<�=7�W�J��> 3?��˿ť:�%�S��́>慿Gb�>!�>�d?�����f>S�>`L ?�R�``	�ș��<��7�1?w��=r y��#�>�4?�}�>�?9�3��\��Ǿ�]�=�.�>�mL<��>��6��A
�Փ�ի�>�To��ye�1������,>�X�>Q����l=h[{=����g�R�����4��?�J� 5U>�Ծ��w��>���s��=��:�ܾkԾ\��D,�?C�H?�W�>`]/��t���AY>�u�>= )���?l?|І=e�*�ŉ�����f)m?&�����>O�>��=���pP�>/�!��]�>�#.>-K=����>C��!K��
����U\?�k�akB?^�=e
,=m�u�S$�����=�SR�p�8?
�-�ʖ�>~x���ì>q�?��о�X�'��Ζ�>^��s&����ƽ���VG׾��[�������?��~��d�B>�=����i)=V!��i�|��>T:I��b����g>��>�bc��ᒿ� J=�ܬ�Ы �gQ�p�r�'ͥ?���?\e���@��e��L��m�>%�Q�Ѩ���(��҆>Ip7���?�cb?ܙ�=.�>#�/�<?/BȽO��>Ԏ��y^������Z��{��>�`�E���\
?��8�Y��>�8�>�c����ɾ'V�V��9������8�;'q?��K�#=F%��5�?!����S>5��E�>��?>sh?ߚp?XC?�\&�@{վ).�>R|?2��=/["=C��>�Ȝ�X/������@]�����ɾ��?n��� R=PR/?9&�>���>㱾�5���6��|Z��r�=}�?<�;�uF���G>w(?�H�Z�(�=*��<�����/Oj�l??��\���>B�8��fy�Bw,��;�HP:?��5�ƽ�;޾r*2� �Ip�>���Q�4�m_4�,/?4M�>�w�!ɐ9�Ԗ�$?Z��>��>��[=X}���?aW�����syJ��m����P"@��c�>j�>=��+�O�k��D��P��ϫ��)������ʞ>��/?���� �Q��o�>���)I����=oS�����>�$�2e?-qT�H4���"?3��=��>��T�D��>wK��ąb>�?27�>��z>Ch�=���= n���?����l��mw�|��*�#�С���H@������7�>E�K?��N����#_�>��D?���>�0M�p�z>�s�+�,?n˫> �O=h�	�r
o��\?�	>� ��X�>�an���6?{|"�PL?"Ɵ��6f>#��>R�D>� ��q�\��7�>�1彙�Z>�&�	��>6��>v
�>�cN�x��?���?["=��>ߝ��k��dRξ���>�:v	�oV�?��>첊���M��T�>A*s>�2�>��@��e޼0U_>k��>�,ݾ?�A>����֖��?�=w���1�>>��-=ɟ��2�=m>�^��ՙ���(=ʺ>�����f��<ٸ����> T��ǅ?U>y+�YgV>�t��WZ=q��>���>X�(>��>��T?:,Z?����{����T�>�;F?3Ib�Z�?0��91�=��=n�k��ѱ>�H0���C?�Ȩ��~�<n��-˾X���cA�9+X?Һ׽<*>��������i�?���?���>�?�>�(=!��>����b�?��G��X?ؤH���>��?���>�F?��1��X�>�T=��!?��e>���|֮���ռ�ɽq(����z>�Ü>��%�l{�>n�ξ�Y���j�N�>�u~?���=�,־]Y?O��=O���E���>�T�<`t=��?/d?|<��0?�`�?l@?r?PCƾ$G�>Gj���6����z�=�|�?��H?{��=�?�>;��G
>�i?��?꽭?�~��4��Ҽ��^(�=�3�/h'>��>��>������=~����??n>�Ӿ�h��-����:�E����o������?rN�<�|?��?:��>R􁾪�7?.sw�!��=ց?Ja���_�?g(�6G?C�?jU�>�[>I��	dN���L�	�>���O���?�tM?X	M�J#�<o�!>|Q"==�>_[����& ����?'�G�=>��p�F>�\=���>�?�z���9!?bژ>@w߽�/?�ö>?�>����4#�� 辆i�<%>��u=��=j�:�}d�>	��>�>�E���<X���iV�������g�>_?�<�෾��6�-u���h?�1���o�;I��>�!W>�#���P�tw?�%���`W�M༉'�?�5���˼v�ξ(<��e�оs����X�>�ޚ>3k�^��>� =Ӻ�(Y�=j��>$3��s�@?,_,=;�� �#��7�>�o����0��<U�v>���>� ?�$��5�/?6����뾙����/�<#,H� �~>&Vk>jq>#�F���+>���>Û�=�
+�녬>�W?:8,?y��w"�>82��x�>�5�>?u+���>��(>�ܾ�`�=<��#��?�lJ���V>�,=��w@���={%��5��>{��>��L��l�GS���Y�{�#�+�j>y�?�z?>h��=�W徤��>[���B?��?̖$?Q�ʾ��>�:�>�<P�M*���U?��޾�����<�
��>'ܾm�>j69��p���p�Y�h=de(���<^e*��SJ��g9>�d
?���>4%���?�ܢ>�T����U����n���t,��m�>2��?U V��e?II�7џ���3��hh?|�?h�>Iڂ?su>]& �n7~>�������7f�=uђ>$��>��a��?a��>�E���>@��?�M�>�i˾�G"=Î?����>1M6��ל<-��� ������*���龿���aј���?�<3��>'��?�]:�ᨿ9�>��(�wk�=��(���P�:?v}?����|��?�Y�U��=�pb>��X=�>�2<�|k��I
�D,c���>����2�>iY>���6�3?�^��M�>���>
F
mulMulVariable/readmul/y*
T0*
_output_shapes	
:�
F
addAddmulVariable_1/read*
_output_shapes	
:�*
T0
�
sub/yConst*
dtype0*
_output_shapes	
:�*�
value�B��"��!�>7��>��.>��>�ȋ>BVn>+?�>g^>�$�>f��>.$�>�x�>6�\>I��>}c�>�x�>�j}>���>9n�>6n�>�>�nm>�:�>و�>�Y�>�>'T�>c��>���>+OT>�ʀ>AE�>���>��>.��>�O�>�z�>'��>α�>y��>��>V��>2�>tzZ>b�>�O>�܀>޾k>���>D�>1�>�hd>�T>*��>Q��> Q�>�ha>韝>E�>�8�>m��>�1�>���>�V�>�҂>S�>�ޘ>�k>��>4]�> �7>�k�>�h>��>Iv�>a��>��l>��p>�n�>��>���>1�>��> �>x�>��>!�>�>��w>9��>	Y�>P��>:׉>q�>��>Kͦ>	��>%�>���>篂>s�>��>�p�>lr�>s�> �>�>/�r>W�>�w�>��>��>H{>��m>D�>��>���>�>��>��>���>�>! �>B9�>}�n>���>Ľ>r�>�!>p��>�Q�>�P�>R�`>\��>��>�nP>�Ӈ>�(�>��>2̇>��>��>,��>L^�>���>�X�>=w>��>�P�>�$�>��>�ـ>�S�>v޴>m��>���>a��>�#�>�i�>�z�>2��>��>R�>{ؑ>�&�>��>X�>�ݖ>�]�>�=�>���>/F�>�C>U �>-ܩ>w�>C��>��|>5Y�>$��>k��>Bњ>��>�x>���>ή>���>"�g>�;�>b��>�բ>�[>:�>���>`�>�ƒ>�}T>�>
��>��>_N�>���>1;j>jK�>� �>�ʲ>�Kc>���>y�>b�>��_>E��>K�t>�8{>-E�>ngn>ઠ>zM�>m�D>+��>y	v>hѾ>)��>��>��>���>qP�>l=�>"W�>1��>�v�>��d>�)U>^o3>�՗>��J>)8�>��>qǼ>��>��>dǽ>���>�>~>�o�>L$�>�a�>���>1�>8��>Zռ>Y��>���>NY�>�>���>��~>bפ>1-�>� �>V�>>B�>�Fc>Q�>;��>�E>TӠ>���>�צ>��>�<�>�߈>|�>0��>nB>��>>�^�>.��>]�z>�Ч>�2l>�0q>P�>��>���>MiO>[�>�7�>�N>��> �>R.�>%}�>ʗ�>e�>=�>`׃>P��>>H�>]��>v9�>�M�>��t>v�>��>���>;�>�̌>�ŭ>O�=��>�M}>�{�>�>i��>�u�>�m�>gpZ> �>ax>/!�>���>���>N�><u�>fw>�wY>G�>>��>��>�>�ӧ>^��>��>%��>=�l>R��>��y>Z�>��>.H�>x��>�rU>=ܓ>*}5>��>Y��>�G�>_��>$�>�/�>�r�>���># �>�e>�x�>�b>�J�>��>��>V�2>�}6>N �>,�>#�C>�v?>D��>���>�v�>�pU>��V>d�>���>8��>e�?>�*>:��>>��>�j�>�Z�>qI�>%��>��>��^>�z�>���>x>�>t�}>#h�>���>:QS>��>���>��=>�L�>Pb�>ڽ>���>Y� >��r>'��>�x�>Y��>
�'>���>R��>�I�>)�q>!��>�Bt>�ߦ>}�x>Ծ�>�B�>t��>&,�>g�>],�>O��>���>$�>5{�>�α>#��>dJ~>��>-��>�!>�fE>��>���>�^>Ҽ�>�n�>Av�>)6�>�>��u>�>l�>C�>���>���>��>��w>;��>/Sg>i^�>F�>��v>Ъ�>��>Y�>�r�>u��>��\>�h�>�vO>���>A[�>�j>�ʚ>�i>s��>���>��>6�>f�o>v�X>���>���>q>p�>�9>D&�><T�>���>K�>3aw>q�>}$(>(ʗ>�h>2��>]j>��N>䀘>R�>Q+�>�P�>(c>�x�>!3�>x{<>�A�>��>(�>�ߍ>��Q>�>���>k>�ӵ>*�>�t>��>�u�>Rv�>y>-�z>��>?|�>�Ż>R��>�|�>yo�>��>+�>���>�-�>N�>>��>嬀>��>�6�>6��>+�^>�>��^>��G>�U�>F�>��>ڀ�>��>�^�>g1�>	��>ֱ�>w�>nD�>���>U�>��>a��>��~>'e>­�>i��>���>�v�>�G<>^�>��>N�>ȉ�>�G�>^D�>�>��c>m��>�	�>�c�>�è>�M�>j��>��>wTp>u�>��>g��>�;u>��>�݇>��0>Ӓ�>+�>�"�>W�>'��>�"�>F>>��p>�A�>�x�>J��>��5>:9�>ä>��>qӆ>��>$��>�>���>å>�\�>�k�>fy>�)�>�>�?�>�>6�>b4�>��m>�z>�I�>��:>�!�>�A?>$�>}S�>�Gi>�߫>�$.>a)�>,w�>d�>ä>���>k��>2��>��>v�>��>7��>9�>ѴE>�S�>��>�,�>��b>U�>�%�>�zd>\�>��>�҉>��q>j��>w�l>$~s>Zw�>��z>KՉ>(Ӏ>K�q>�>��>�%�>�>��>���>�>.>"�>�>���>�17>�w�>a��>�>���>)Zu>�:�>���>\w�>��>;(N> �>.��>Oj�>,>+T�>��>Im�>�ѕ>rY>�F�>a{�>�.�>���>�(�>s�s>[n�>�
�>ߟ>�߄>���>�8�>h�>��>M��>���>'��>q�>>��>�S�>M<�>;`�>:P>p��>i�~>侣>�h�>쯺>/v�>t�>�Ҝ>�TY>�t�>B�>�!�>T�>N�>�>:hu>�
�>�א>���>��>f�>�0>��p>ٍ>��>Dd�>1�>�{]>y�B>�v>�4g>��>���>��> P�>�d�>�)�>|.�>ѿ�>�3�>�I>�\�>l��>�'�>�>��R>f�>��>iG�>:إ>�A�>C
�>E4}>4�}>�>�6�>�K�>@_>SP�>&;�>Ij�>e�>��>�؅>�xK>SԻ>ꖉ>��>-|>�>�w>S�>O��>��>+�>k�>�$�>��>x��><D�>���>�P>0�>�8�>��W>sz�>���>�:}>=N�>�>I��>��>�ɢ>�p>Gφ>��>)q�>g�>ɴ�>�p�>���>�te>9b�>+�}>���>�5�>�>�}r>�>�e�>dk�>�MT>긋>�7�>D�>R�>~5z>t~e>sg>�U�>% �>෍>�r.>h��>�:�>�k�>�~�>�>�M�>��>r�>��f>uu{>��>�:�>��|>�c�>H��>Į�>��>Cj�>�>�Na>�"�>�8�>@]�>ʀR>���>Ƙ�>�4�>ln�>�`�>���>;�>+m>؜�>��>f��>.�@>(o�>7�T>��>C<�>�Oo>���>7��>�_>s��>��>�(�>SP}>BX�>R�T>g'h>��>i��>�N�>g,�>�_>X<r>c�>��>Q`N>��>��>ҥ�>��>��>)�i>_�>�bt>�(�>3q�>�b�>�e�>��>�p�>�=T>�c�>�M�>�#�>�É>��=>K��>)�]>N%�>��>��8>�]>��>�b>��>B�>!m_>���>x��>ב�>.��>�.�>�>&�>R��=�Za>^^�>�|�>-��>��>Ax>�>:�Z>�o�>]F>�Z�>bS�>\�>���>Uڴ>vG�>^=�>I�>n/P>�H�>셝>���>j�>�@�>v�>��c>r4�>*�>1�>>R�>¯�>���>O�>��L>pS�>-i�>��>���>R��>�&�>�i�>�59>���><�>#c�>5��>o�>�>F��>kͤ>��>��>^��>�A�>#z�>lk�>���>x�>8�>�0�>�I�>d��>��l>V�>��C>m>j��>���>�ѳ>��>�	�>�+�>��>2/�>�B�>
<
subSubaddsub/y*
T0*
_output_shapes	
:�
;
SquareSquaresub*
T0*
_output_shapes	
:�
O
ConstConst*
valueB: *
dtype0*
_output_shapes
:
Y
MeanMeanSquareConst*
	keep_dims( *

Tidx0*
T0*
_output_shapes
: 
R
gradients/ShapeConst*
valueB *
dtype0*
_output_shapes
: 
X
gradients/grad_ys_0Const*
valueB
 *  �?*
dtype0*
_output_shapes
: 
o
gradients/FillFillgradients/Shapegradients/grad_ys_0*
T0*

index_type0*
_output_shapes
: 
k
!gradients/Mean_grad/Reshape/shapeConst*
valueB:*
dtype0*
_output_shapes
:
�
gradients/Mean_grad/ReshapeReshapegradients/Fill!gradients/Mean_grad/Reshape/shape*
_output_shapes
:*
T0*
Tshape0
d
gradients/Mean_grad/ConstConst*
valueB:�*
dtype0*
_output_shapes
:
�
gradients/Mean_grad/TileTilegradients/Mean_grad/Reshapegradients/Mean_grad/Const*

Tmultiples0*
T0*
_output_shapes	
:�
`
gradients/Mean_grad/Const_1Const*
dtype0*
_output_shapes
: *
valueB
 *  zD
�
gradients/Mean_grad/truedivRealDivgradients/Mean_grad/Tilegradients/Mean_grad/Const_1*
T0*
_output_shapes	
:�
~
gradients/Square_grad/ConstConst^gradients/Mean_grad/truediv*
dtype0*
_output_shapes
: *
valueB
 *   @
h
gradients/Square_grad/MulMulsubgradients/Square_grad/Const*
T0*
_output_shapes	
:�
�
gradients/Square_grad/Mul_1Mulgradients/Mean_grad/truedivgradients/Square_grad/Mul*
T0*
_output_shapes	
:�
`
gradients/sub_grad/NegNeggradients/Square_grad/Mul_1*
T0*
_output_shapes	
:�
b
#gradients/sub_grad/tuple/group_depsNoOp^gradients/Square_grad/Mul_1^gradients/sub_grad/Neg
�
+gradients/sub_grad/tuple/control_dependencyIdentitygradients/Square_grad/Mul_1$^gradients/sub_grad/tuple/group_deps*
T0*.
_class$
" loc:@gradients/Square_grad/Mul_1*
_output_shapes	
:�
�
-gradients/sub_grad/tuple/control_dependency_1Identitygradients/sub_grad/Neg$^gradients/sub_grad/tuple/group_deps*
_output_shapes	
:�*
T0*)
_class
loc:@gradients/sub_grad/Neg
c
gradients/add_grad/ShapeConst*
valueB:�*
dtype0*
_output_shapes
:
d
gradients/add_grad/Shape_1Const*
valueB:*
dtype0*
_output_shapes
:
�
(gradients/add_grad/BroadcastGradientArgsBroadcastGradientArgsgradients/add_grad/Shapegradients/add_grad/Shape_1*
T0*2
_output_shapes 
:���������:���������
�
gradients/add_grad/SumSum+gradients/sub_grad/tuple/control_dependency(gradients/add_grad/BroadcastGradientArgs*
_output_shapes	
:�*
	keep_dims( *

Tidx0*
T0
�
gradients/add_grad/ReshapeReshapegradients/add_grad/Sumgradients/add_grad/Shape*
_output_shapes	
:�*
T0*
Tshape0
�
gradients/add_grad/Sum_1Sum+gradients/sub_grad/tuple/control_dependency*gradients/add_grad/BroadcastGradientArgs:1*
T0*
_output_shapes
: *
	keep_dims( *

Tidx0
�
gradients/add_grad/Reshape_1Reshapegradients/add_grad/Sum_1gradients/add_grad/Shape_1*
T0*
Tshape0*
_output_shapes
:
g
#gradients/add_grad/tuple/group_depsNoOp^gradients/add_grad/Reshape^gradients/add_grad/Reshape_1
�
+gradients/add_grad/tuple/control_dependencyIdentitygradients/add_grad/Reshape$^gradients/add_grad/tuple/group_deps*
_output_shapes	
:�*
T0*-
_class#
!loc:@gradients/add_grad/Reshape
�
-gradients/add_grad/tuple/control_dependency_1Identitygradients/add_grad/Reshape_1$^gradients/add_grad/tuple/group_deps*
_output_shapes
:*
T0*/
_class%
#!loc:@gradients/add_grad/Reshape_1
b
gradients/mul_grad/ShapeConst*
valueB:*
dtype0*
_output_shapes
:
e
gradients/mul_grad/Shape_1Const*
dtype0*
_output_shapes
:*
valueB:�
�
(gradients/mul_grad/BroadcastGradientArgsBroadcastGradientArgsgradients/mul_grad/Shapegradients/mul_grad/Shape_1*2
_output_shapes 
:���������:���������*
T0
w
gradients/mul_grad/MulMul+gradients/add_grad/tuple/control_dependencymul/y*
T0*
_output_shapes	
:�
�
gradients/mul_grad/SumSumgradients/mul_grad/Mul(gradients/mul_grad/BroadcastGradientArgs*
T0*
_output_shapes
: *
	keep_dims( *

Tidx0
�
gradients/mul_grad/ReshapeReshapegradients/mul_grad/Sumgradients/mul_grad/Shape*
T0*
Tshape0*
_output_shapes
:
�
gradients/mul_grad/Mul_1MulVariable/read+gradients/add_grad/tuple/control_dependency*
T0*
_output_shapes	
:�
�
gradients/mul_grad/Sum_1Sumgradients/mul_grad/Mul_1*gradients/mul_grad/BroadcastGradientArgs:1*
T0*
_output_shapes	
:�*
	keep_dims( *

Tidx0
�
gradients/mul_grad/Reshape_1Reshapegradients/mul_grad/Sum_1gradients/mul_grad/Shape_1*
T0*
Tshape0*
_output_shapes	
:�
g
#gradients/mul_grad/tuple/group_depsNoOp^gradients/mul_grad/Reshape^gradients/mul_grad/Reshape_1
�
+gradients/mul_grad/tuple/control_dependencyIdentitygradients/mul_grad/Reshape$^gradients/mul_grad/tuple/group_deps*
T0*-
_class#
!loc:@gradients/mul_grad/Reshape*
_output_shapes
:
�
-gradients/mul_grad/tuple/control_dependency_1Identitygradients/mul_grad/Reshape_1$^gradients/mul_grad/tuple/group_deps*
T0*/
_class%
#!loc:@gradients/mul_grad/Reshape_1*
_output_shapes	
:�
b
GradientDescent/learning_rateConst*
valueB
 *   ?*
dtype0*
_output_shapes
: 
�
4GradientDescent/update_Variable/ApplyGradientDescentApplyGradientDescentVariableGradientDescent/learning_rate+gradients/mul_grad/tuple/control_dependency*
T0*
_class
loc:@Variable*
_output_shapes
:*
use_locking( 
�
6GradientDescent/update_Variable_1/ApplyGradientDescentApplyGradientDescent
Variable_1GradientDescent/learning_rate-gradients/add_grad/tuple/control_dependency_1*
T0*
_class
loc:@Variable_1*
_output_shapes
:*
use_locking( 
�
GradientDescentNoOp5^GradientDescent/update_Variable/ApplyGradientDescent7^GradientDescent/update_Variable_1/ApplyGradientDescent
\
cost_scalar/tagsConst*
valueB Bcost_scalar*
dtype0*
_output_shapes
: 
U
cost_scalarScalarSummarycost_scalar/tagsMean*
T0*
_output_shapes
: 
P
Merge/MergeSummaryMergeSummarycost_scalar*
N*
_output_shapes
: 
2
initNoOp^Variable/Assign^Variable_1/Assign""�
trainable_variables��
B

Variable:0Variable/AssignVariable/read:02random_uniform:08
?
Variable_1:0Variable_1/AssignVariable_1/read:02zeros:08"
	summaries

cost_scalar:0"
train_op

GradientDescent"�
	variables��
B

Variable:0Variable/AssignVariable/read:02random_uniform:08
?
Variable_1:0Variable_1/AssignVariable_1/read:02zeros:082xB       QKD	�Fo��A*

cost_scalar�&�::i��!       {��	Fo��A
*

cost_scalarSp:A�V?!       {��	��Fo��A*

cost_scalar�Dp: V!       {��	�	Fo��A*

cost_scalar�Dp:��m!       {��	ρFo��A(*

cost_scalar�Dp:���P!       {��	c�Fo��A2*

cost_scalar�Dp:6G��!       {��	�bFo��A<*

cost_scalar�Dp:��jk!       {��	��Fo��AF*

cost_scalar�Dp:�lX�!       {��	#�Fo��AP*

cost_scalar�Dp:�A!:!       {��	`Fo��AZ*

cost_scalar�Dp:Ќw!       {��	��Fo��Ad*

cost_scalar�Dp:r�֠