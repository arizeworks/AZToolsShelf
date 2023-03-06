import bpy

#################################################
############## Render Presets ###################
#################################################

##### Preferences #####
bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'
##### Render-Settings #####
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.render.use_stamp = False
# Performance
bpy.context.scene.render.use_high_quality_normals = False
bpy.context.scene.render.hair_type = 'STRAND'
bpy.context.scene.render.hair_subdiv = 0
# Film
bpy.context.scene.render.filter_size = 1.5
bpy.context.scene.render.film_transparent = True
bpy.context.scene.render.use_simplify = True
bpy.context.scene.render.simplify_subdivision = 6
bpy.context.scene.render.simplify_child_particles = 1.0
bpy.context.scene.render.simplify_volumes = 1.0
bpy.context.scene.render.simplify_subdivision_render = 6
bpy.context.scene.render.simplify_child_particles_render = 1.0
bpy.context.scene.render.simplify_gpencil = False
bpy.context.scene.render.simplify_gpencil_onplay = False
bpy.context.scene.render.simplify_gpencil_view_fill = True
bpy.context.scene.render.simplify_gpencil_modifier = True
bpy.context.scene.render.simplify_gpencil_shader_fx = True
bpy.context.scene.render.simplify_gpencil_tint = True
bpy.context.scene.render.simplify_gpencil_antialiasing = True
# Freestyle
bpy.context.scene.render.use_freestyle = False
bpy.context.scene.render.line_thickness_mode = 'ABSOLUTE'
bpy.context.scene.render.line_thickness = 1.0
# Color Management
bpy.context.scene.display_settings.display_device = 'sRGB'
bpy.context.scene.view_settings.view_transform = 'Standard'
bpy.context.scene.view_settings.look = 'None'
bpy.context.scene.view_settings.exposure = 0.0
bpy.context.scene.view_settings.gamma = 1.0
bpy.context.scene.sequencer_colorspace_settings.name = 'sRGB'
##### EEVEE-Settings #####
# Sampling
bpy.context.scene.eevee.taa_render_samples = 128
bpy.context.scene.eevee.taa_samples = 128
bpy.context.scene.eevee.use_taa_reprojection = True
# Ambient Occlusion
bpy.context.scene.eevee.use_gtao = False
bpy.context.scene.eevee.gtao_distance = 0.20000000298023224
bpy.context.scene.eevee.gtao_factor = 1.0
bpy.context.scene.eevee.gtao_quality = 0.25
bpy.context.scene.eevee.use_gtao_bent_normals = True
bpy.context.scene.eevee.use_gtao_bounce = True
# Bloom
bpy.context.scene.eevee.use_bloom = False
bpy.context.scene.eevee.bloom_threshold = 0.8999999761581421
bpy.context.scene.eevee.bloom_knee = 0.5
bpy.context.scene.eevee.bloom_radius = 6.5
bpy.context.scene.eevee.bloom_color.r = 1.0
bpy.context.scene.eevee.bloom_color.g = 1.0
bpy.context.scene.eevee.bloom_color.b = 1.0
bpy.context.scene.eevee.bloom_intensity = 0.05000000074505806
bpy.context.scene.eevee.bloom_clamp = 0.0
# Depth of Field
bpy.context.scene.eevee.bokeh_threshold = 1.0
bpy.context.scene.eevee.bokeh_neighbor_max = 10.0
bpy.context.scene.eevee.bokeh_denoise_fac = 0.75
bpy.context.scene.eevee.use_bokeh_high_quality_slight_defocus = False
bpy.context.scene.eevee.use_bokeh_jittered = False
bpy.context.scene.eevee.bokeh_overblur = 5.0
bpy.context.scene.eevee.bokeh_max_size = 100.0
bpy.context.scene.eevee.sss_samples = 7
bpy.context.scene.eevee.sss_jitter_threshold = 0.30000001192092896
# Screen Space Reflection
bpy.context.scene.eevee.use_ssr = True
bpy.context.scene.eevee.use_ssr_halfres = True
bpy.context.scene.eevee.use_ssr_refraction = True
bpy.context.scene.eevee.ssr_quality = 0.25
bpy.context.scene.eevee.ssr_max_roughness = 0.5
bpy.context.scene.eevee.ssr_thickness = 0.20000000298023224
bpy.context.scene.eevee.ssr_border_fade = 0.07500000298023224
bpy.context.scene.eevee.ssr_firefly_fac = 10.0
# Motion Blur
bpy.context.scene.eevee.use_motion_blur = False
bpy.context.scene.eevee.motion_blur_position = 'CENTER'
bpy.context.scene.eevee.motion_blur_shutter = 15.0
bpy.context.scene.eevee.motion_blur_depth_scale = 100.0
bpy.context.scene.eevee.motion_blur_max = 32
bpy.context.scene.eevee.motion_blur_steps = 1
# Voluminetrics
bpy.context.scene.eevee.volumetric_start = 0.10000000149011612
bpy.context.scene.eevee.volumetric_end = 100.0
bpy.context.scene.eevee.volumetric_tile_size = '8'
bpy.context.scene.eevee.volumetric_samples = 64
bpy.context.scene.eevee.volumetric_sample_distribution = 0.800000011920929
bpy.context.scene.eevee.use_volumetric_lights = True
bpy.context.scene.eevee.volumetric_light_clamp = 0.0
bpy.context.scene.eevee.use_volumetric_shadows = False
bpy.context.scene.eevee.volumetric_shadow_samples = 16
# Shadows
bpy.context.scene.eevee.shadow_cube_size = '64'
bpy.context.scene.eevee.shadow_cascade_size = '64'
bpy.context.scene.eevee.use_shadow_high_bitdepth = True
bpy.context.scene.eevee.use_soft_shadows = False
bpy.context.scene.eevee.light_threshold = 0.009999999776482582
# Indirect Lightning
bpy.context.scene.eevee.gi_auto_bake = False
bpy.context.scene.eevee.gi_diffuse_bounces = 3
bpy.context.scene.eevee.gi_cubemap_resolution = '512'
bpy.context.scene.eevee.gi_visibility_resolution = '32'
bpy.context.scene.eevee.gi_irradiance_smoothing = 0.10000000149011612
bpy.context.scene.eevee.gi_glossy_clamp = 0.0
bpy.context.scene.eevee.gi_filter_quality = 1.0
bpy.context.scene.eevee.gi_cubemap_display_size = 0.30000001192092896
bpy.context.scene.eevee.gi_irradiance_display_size = 0.10000000149011612
bpy.context.scene.eevee.gi_show_cubemaps = False
bpy.context.scene.eevee.gi_show_irradiance = False
##### CYCLES-Settings #####
bpy.context.scene.cycles.feature_set = 'SUPPORTED'
bpy.context.scene.cycles.device = 'CPU'
bpy.context.scene.cycles.shading_system = True
# Sampling 
bpy.context.scene.cycles.samples = 1
bpy.context.scene.cycles.preview_samples = 1
bpy.context.scene.cycles.use_adaptive_sampling = False
bpy.context.scene.cycles.adaptive_threshold = 0.0
bpy.context.scene.cycles.adaptive_min_samples = 0
bpy.context.scene.cycles.use_preview_adaptive_sampling = False
bpy.context.scene.cycles.preview_adaptive_threshold = 0.10000000149011612
bpy.context.scene.cycles.preview_adaptive_min_samples = 0
bpy.context.scene.cycles.use_preview_denoising = False
bpy.context.scene.cycles.preview_denoiser = 'AUTO'
bpy.context.scene.cycles.preview_denoising_input_passes = 'RGB_ALBEDO'
bpy.context.scene.cycles.preview_denoising_start_sample = 1
bpy.context.scene.cycles.time_limit = 0.0
bpy.context.scene.cycles.use_denoising = False
bpy.context.scene.cycles.denoiser = 'OPENIMAGEDENOISE'
bpy.context.scene.cycles.denoising_input_passes = 'RGB_ALBEDO_NORMAL'
bpy.context.scene.cycles.denoising_prefilter = 'ACCURATE'
bpy.context.scene.cycles.seed = 0
bpy.context.scene.cycles.use_animated_seed = False
bpy.context.scene.cycles.sampling_pattern = 'PROGRESSIVE_MULTI_JITTER'
bpy.context.scene.cycles.scrambling_distance = 1.0
bpy.context.scene.cycles.preview_scrambling_distance = False
bpy.context.scene.cycles.min_light_bounces = 0
bpy.context.scene.cycles.min_transparent_bounces = 0
bpy.context.scene.cycles.light_sampling_threshold = 0.009999999776482582
# Denoising 
bpy.context.scene.cycles.use_denoising = False
bpy.context.scene.cycles.denoiser = 'OPENIMAGEDENOISE'
bpy.context.scene.cycles.use_preview_denoising = False
bpy.context.scene.cycles.preview_denoiser = 'AUTO'
bpy.context.scene.cycles.preview_denoising_start_sample = 1
bpy.context.scene.cycles.preview_denoising_input_passes = 'RGB_ALBEDO'
# Advanced 
bpy.context.scene.cycles.seed = 0
bpy.context.scene.cycles.use_animated_seed = False
bpy.context.scene.cycles.sampling_pattern = 'PROGRESSIVE_MULTI_JITTER'
bpy.context.scene.cycles.min_light_bounces = 0
bpy.context.scene.cycles.min_transparent_bounces = 0
bpy.context.scene.cycles.light_sampling_threshold = 0.009999999776482582
# Light Paths
bpy.context.scene.cycles.max_bounces = 1
bpy.context.scene.cycles.diffuse_bounces = 1
bpy.context.scene.cycles.glossy_bounces = 1
bpy.context.scene.cycles.transparent_max_bounces = 1
bpy.context.scene.cycles.transmission_bounces = 1
bpy.context.scene.cycles.volume_bounces = 0
bpy.context.scene.cycles.sample_clamp_direct = 0.0
bpy.context.scene.cycles.sample_clamp_indirect = 10.0
bpy.context.scene.cycles.blur_glossy = 1.0
bpy.context.scene.cycles.caustics_reflective = True
bpy.context.scene.cycles.caustics_refractive = True
bpy.context.scene.cycles.use_fast_gi = False
bpy.context.scene.world.light_settings.ao_factor = 1.0
bpy.context.scene.world.light_settings.distance = 10.0
# Volumes 
bpy.context.scene.cycles.volume_step_rate = 1.0
bpy.context.scene.cycles.volume_preview_step_rate = 1.0
bpy.context.scene.cycles.volume_max_steps = 1024
# Subdivision
bpy.context.scene.cycles.dicing_rate = 1.0
bpy.context.scene.cycles.preview_dicing_rate = 8.0
bpy.context.scene.cycles.offscreen_dicing_scale = 4.0
bpy.context.scene.cycles.max_subdivisions = 12
bpy.context.scene.cycles.dicing_camera = None
# Hair
bpy.context.scene.cycles_curves.shape = 'RIBBONS'
bpy.context.scene.cycles_curves.subdivisions = 2
# Simplify
bpy.context.scene.render.use_simplify = True
bpy.context.scene.render.simplify_subdivision = 6
bpy.context.scene.render.simplify_child_particles = 1.0
bpy.context.scene.cycles.texture_limit = 'OFF'
bpy.context.scene.cycles.ao_bounces = 0
bpy.context.scene.render.simplify_volumes = 1.0
bpy.context.scene.render.simplify_subdivision_render = 6
bpy.context.scene.render.simplify_child_particles_render = 1.0
bpy.context.scene.cycles.texture_limit_render = 'OFF'
bpy.context.scene.cycles.ao_bounces_render = 0
# Motion Blur
bpy.context.scene.render.use_motion_blur = False
bpy.context.scene.cycles.motion_blur_position = 'CENTER'
bpy.context.scene.render.motion_blur_shutter = 0.5
bpy.context.scene.cycles.rolling_shutter_type = 'NONE'
bpy.context.scene.cycles.rolling_shutter_duration = 0.10000000149011612
# Film
bpy.context.scene.cycles.film_exposure = 1.0
bpy.context.scene.cycles.pixel_filter_type = 'BLACKMAN_HARRIS'
bpy.context.scene.cycles.filter_width = 1.5
bpy.context.scene.render.film_transparent = True
bpy.context.scene.cycles.film_transparent_glass = False
bpy.context.scene.cycles.film_transparent_roughness = 0.10000000149011612
# Performance
bpy.context.scene.render.threads_mode = 'AUTO'
bpy.context.scene.render.threads = 16
bpy.context.scene.cycles.tile_size = 2048
bpy.context.scene.cycles.debug_use_spatial_splits = False
bpy.context.scene.cycles.debug_use_compact_bvh = False
bpy.context.scene.cycles.debug_use_hair_bvh = True
bpy.context.scene.cycles.debug_bvh_time_steps = 0
bpy.context.scene.render.use_persistent_data = True
bpy.context.scene.render.preview_pixel_size = 'AUTO'
# Bake
bpy.context.scene.render.use_bake_multires = False
bpy.context.scene.cycles.bake_type = 'COMBINED'
bpy.context.scene.render.bake.use_pass_direct = True
bpy.context.scene.render.bake.use_pass_indirect = True
bpy.context.scene.render.bake.use_pass_diffuse = True
bpy.context.scene.render.bake.use_pass_glossy = True
bpy.context.scene.render.bake.use_pass_transmission = True
bpy.context.scene.render.bake.use_pass_emit = True
bpy.context.scene.render.bake.use_selected_to_active = False
bpy.context.scene.render.bake.use_cage = False
bpy.context.scene.render.bake.cage_object = None
bpy.context.scene.render.bake.cage_extrusion = 0.0
bpy.context.scene.render.bake.max_ray_distance = 0.0
bpy.context.scene.render.bake.margin = 16
bpy.context.scene.render.bake.margin_type = 'ADJACENT_FACES'
bpy.context.scene.render.bake.use_clear = True
# Grease Pencil
bpy.context.scene.grease_pencil_settings.antialias_threshold = 1.0
bpy.context.scene.render.line_thickness_mode = 'ABSOLUTE'
bpy.context.scene.render.line_thickness = 1.0
##### WORKBENCH ##########
bpy.context.scene.grease_pencil_settings.antialias_threshold = 1.0
bpy.context.scene.render.use_high_quality_normals = False
# Sampling
bpy.context.scene.display.render_aa = '8'
bpy.context.scene.display.viewport_aa = 'FXAA'
# Lighting
bpy.context.scene.display.shading.light = 'STUDIO'
bpy.context.scene.display.shading.studio_light = 'Default'
bpy.context.scene.display.shading.use_world_space_lighting = False
bpy.context.scene.display.shading.studiolight_rotate_z = 0.0
# Color
bpy.context.scene.display.shading.color_type = 'MATERIAL'
# Options
bpy.context.scene.display.shading.show_backface_culling = False
bpy.context.scene.display.shading.show_xray = False
bpy.context.scene.display.shading.xray_alpha = 0.5
bpy.context.scene.display.shading.show_shadows = False
bpy.context.scene.display.shading.shadow_intensity = 0.5
bpy.context.scene.display.light_direction.x = 0.5773502588272095
bpy.context.scene.display.light_direction.y = 0.5773502588272095
bpy.context.scene.display.light_direction.z = 0.5773502588272095
bpy.context.scene.display.shadow_shift = 0.10000000149011612
bpy.context.scene.display.shadow_focus = 0.0
bpy.context.scene.display.shading.show_cavity = False
bpy.context.scene.display.shading.cavity_type = 'WORLD'
bpy.context.scene.display.shading.cavity_ridge_factor = 1.0
bpy.context.scene.display.shading.cavity_valley_factor = 1.0
bpy.context.scene.display.matcap_ssao_samples = 16
bpy.context.scene.display.matcap_ssao_distance = 0.20000000298023224
bpy.context.scene.display.matcap_ssao_attenuation = 1.0
bpy.context.scene.display.shading.curvature_ridge_factor = 0.0
bpy.context.scene.display.shading.curvature_valley_factor = 0.0
bpy.context.scene.display.shading.use_dof = False
bpy.context.scene.display.shading.show_object_outline = False
bpy.context.scene.display.shading.object_outline_color.r = 0.0
bpy.context.scene.display.shading.object_outline_color.g = 0.0
bpy.context.scene.display.shading.object_outline_color.b = 0.0
bpy.context.scene.display.shading.show_specular_highlight = True
# Film
bpy.context.scene.render.film_transparent = True
##### OUTPUT PROPERTIES #####
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.render.pixel_aspect_x = 1.0
bpy.context.scene.render.pixel_aspect_y = 1.0
bpy.context.scene.render.use_border = False
bpy.context.scene.render.use_crop_to_border = False
bpy.context.scene.frame_step = 1
bpy.context.scene.render.fps = 24
bpy.context.scene.render.frame_map_old = 100
bpy.context.scene.render.frame_map_new = 100
# Stereoscopy
bpy.context.scene.render.use_multiview = False
bpy.context.scene.render.views_format = 'STEREO_3D'
bpy.context.scene.render.views['left'].use = True
bpy.context.scene.render.views['right'].use = True
bpy.context.scene.render.views['left'].file_suffix = '_L'
bpy.context.scene.render.views['right'].file_suffix = '_R'
# Output
# Images + Video
bpy.context.scene.render.use_file_extension = True
bpy.context.scene.render.use_render_cache = False
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.image_settings.color_mode = 'RGBA'
bpy.context.scene.render.image_settings.views_format = 'INDIVIDUAL'
bpy.context.scene.render.image_settings.compression = 15
bpy.context.scene.render.image_settings.quality = 90
bpy.context.scene.render.image_settings.jpeg2k_codec = 'JP2'
bpy.context.scene.render.image_settings.use_jpeg2k_cinema_preset = False
bpy.context.scene.render.image_settings.use_jpeg2k_cinema_48 = False
bpy.context.scene.render.image_settings.use_jpeg2k_ycc = False
bpy.context.scene.render.image_settings.use_cineon_log = False
bpy.context.scene.render.image_settings.color_depth = '8'
bpy.context.scene.render.image_settings.exr_codec = 'ZIP'
bpy.context.scene.render.image_settings.use_zbuffer = False
bpy.context.scene.render.image_settings.use_preview = False
bpy.context.scene.render.use_overwrite = True
bpy.context.scene.render.use_placeholder = False
bpy.context.scene.render.image_settings.tiff_codec = 'DEFLATE'
# FFmpeg Video
bpy.context.scene.render.ffmpeg.format = 'MPEG1'
bpy.context.scene.render.ffmpeg.use_autosplit = False
bpy.context.scene.render.ffmpeg.codec = 'NONE'
bpy.context.scene.render.ffmpeg.constant_rate_factor = 'NONE'
bpy.context.scene.render.ffmpeg.ffmpeg_preset = 'GOOD'
bpy.context.scene.render.ffmpeg.gopsize = 0
bpy.context.scene.render.ffmpeg.use_max_b_frames = False
bpy.context.scene.render.ffmpeg.max_b_frames = 0
bpy.context.scene.render.ffmpeg.audio_codec = 'NONE'
bpy.context.scene.render.ffmpeg.audio_channels = 'STEREO'
bpy.context.scene.render.ffmpeg.audio_mixrate = 48000
bpy.context.scene.render.ffmpeg.audio_bitrate = 192
bpy.context.scene.render.ffmpeg.audio_volume = 1.0
bpy.context.scene.render.ffmpeg.video_bitrate = 0
bpy.context.scene.render.ffmpeg.minrate = 0
bpy.context.scene.render.ffmpeg.maxrate = 0
bpy.context.scene.render.ffmpeg.buffersize = 0
bpy.context.scene.render.ffmpeg.muxrate = 0
bpy.context.scene.render.ffmpeg.packetsize = 0
bpy.context.scene.render.ffmpeg.use_lossless_output = False
# Metadata
bpy.context.scene.render.metadata_input = 'SCENE'
bpy.context.scene.render.use_stamp_date = True
bpy.context.scene.render.use_stamp_time = True
bpy.context.scene.render.use_stamp_render_time = True
bpy.context.scene.render.use_stamp_frame = True
bpy.context.scene.render.use_stamp_frame_range = False
bpy.context.scene.render.use_stamp_memory = False
bpy.context.scene.render.use_stamp_hostname = False
bpy.context.scene.render.use_stamp_camera = True
bpy.context.scene.render.use_stamp_lens = False
bpy.context.scene.render.use_stamp_scene = True
bpy.context.scene.render.use_stamp_marker = False
bpy.context.scene.render.use_stamp_filename = True
# Post Processing
bpy.context.scene.render.use_compositing = True
bpy.context.scene.render.use_sequencer = True
bpy.context.scene.render.dither_intensity = 1.0


